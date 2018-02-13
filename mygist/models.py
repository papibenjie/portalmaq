from django.db import models



class Gist(models.Model):
    """docstring for Gist."""
    SUITE = "Suite"
    SORT = "Sort"
    UTIL = "Util"
    NONE = "None"

    CATEGORY = (
        (SUITE, SUITE),
        (SORT, SORT),
        (UTIL, UTIL),
        (NONE, NONE),
    )
    gid = models.SlugField(primary_key=True)
    creator = models.CharField(max_length=50, default="")
    commentary = models.CharField(max_length=300, default="")
    category = models.CharField(max_length=10, choices=CATEGORY, default=NONE)

    def get_embded(self):
        return "https://gist.github.com/{0}/{1}.js".format(self.creator, self.gid)

    def __str__(self):
        return "{0} [Id: {1}, Author: {2}, Comment: {3}, Category: {4}]".format(self.__class__.__name__, self.gid, self.creator, self.commentary, self.category)
