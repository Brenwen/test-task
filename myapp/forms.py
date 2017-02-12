from django import forms
from django.contrib.postgres.forms import JSONField
from django.forms import CharField

from myapp.models import MyJSONModel


class MyForm(forms.ModelForm):


    class Meta:
       model = MyJSONModel
       exclude = [""]
