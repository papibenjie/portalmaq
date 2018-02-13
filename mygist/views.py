from django.http import HttpResponse
from django.template import loader

from .models import Gist

import urllib3
import requests

def refresh_user_gists(username):
    r = requests.get('https://api.github.com/users/{0}/gists'.format(username))
    for i in r.json():
        g = Gist(gid=i["id"], creator=i["owner"]["login"], commentary=str(i["description"]) )
        g.save()

def user_category_gists(request, username, category):
    template = loader.get_template('mygist/index.html')
    context = {"gists": Gist.objects.filter(creator=username, category=category),}
    return HttpResponse(template.render(context, request))

def category_gists(request, category):
    template = loader.get_template('mygist/index.html')
    context = {"gists": Gist.objects.filter(category=category)}
    return HttpResponse(template.render(context, request))

def user_gists(request, username):
    template = loader.get_template('mygist/index.html')
    context = {"gists": Gist.objects.filter(creator=username)}
    return HttpResponse(template.render(context, request))

def index(request):
    return user_gists(request, "papibenjie")
