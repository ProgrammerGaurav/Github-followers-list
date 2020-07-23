from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=50)
