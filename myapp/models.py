import json

from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class MyJSONModel(models.Model):
    json_names = JSONField(default=dict)

    def __str__(self):
        return json.dumps(self.json_names)