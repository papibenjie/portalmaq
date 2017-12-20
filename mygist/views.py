from django.http import HttpResponse
from django.template import loader

from .models import Gist

import urllib3
import requests


def index(request):
    template = loader.get_template('mygist/index.html')
    gist_urls = {}
    username = "papibenjie"

    r = requests.get('https://api.github.com/users/'+username+'/gists')


    for i in r.json():
        commentary = ""
        if len(Gist.objects.filter(gid=i["id"])) <= 0:
            g = Gist(gid=i["id"], commentary="Not yet...")
            g.save()
        for j in Gist.objects.filter(gid=i["id"]):
            commentary = j.commentary
        gist_urls[("https://gist.github.com/{0}/{1}.js".format(username, i["id"]))] = commentary
    print(gist_urls)
    context = {
        "gist_urls":gist_urls,
    }
    return HttpResponse(template.render(context, request))
