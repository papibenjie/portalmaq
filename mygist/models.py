from django.db import models

class Gist(models.Model):
    """docstring for Gist."""
    gid = models.CharField(max_length=50)
    commentary = models.CharField(max_length=300, default="")

    def get_commentary(self):
        pass
