from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.fields import data


class Entry(models.Model):
    Id = data.IntField(pk=True)
    RegNumber = data.CharField(50, unique=True)
    Date = data.DateField()
    Organ = data.CharField(500, null=True)
    Address = data.CharField(500, null=True)
    Content = data.CharField(500, null=True)
    Sender = data.CharField(500, null=True)
    Wey = data.CharField(500, null=True)
    Files = data.CharField(500, null=True)

Entry_Pydantic = pydantic_model_creator(Entry, name="Entry")
EntryIn_Pydantic = pydantic_model_creator(Entry, name="EntryIn", exclude_readonly=True)