from django.db import models
from django.contrib.postgres.fields import JSONField


class GenericModel(models.Model):
    title = models.CharField(max_length=32, null=False)
    data = JSONField()
    scheme = JSONField()

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        pass

    def __str__(self):
        return self.title
