import ast
from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    pro_name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class model_user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    profile_name = models.CharField(max_length=100)
    id = models.CharField(unique=True, max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    hash_id = models.CharField(max_length=100)
    age = models.IntegerField(default=0, blank=True)
    age_status = models.CharField(max_length=100, default="below 20")


class model_form(models.Model):
    postedBy = models.CharField(max_length=100)
    subForum = models.CharField(max_length=100, default='')
    upVotes = models.IntegerField(default=0, blank=True)
    downVotes = models.IntegerField(default=0, blank=True)
    bodyText = models.TextField(default='')
    bodyImage = models.CharField(default='', max_length=100, blank=True)
    uVoted = models.BooleanField(default=False)
    dVoted = models.BooleanField(default=False)


class model_chat_thread(models.Model):
    name = models.CharField(max_length=100)


# class ListField(models.TextField):
#     __metaclass__ = models.SubfieldBase
#     description = "Stores a python list"

#     def __init__(self, *args, **kwargs):
#         super(ListField, self).__init__(*args, **kwargs)

#     def to_python(self, value):
#         if not value:
#             value = []

#         if isinstance(value, list):
#             return value

#         return ast.literal_eval(value)

#     def get_prep_value(self, value):
#         if value is None:
#             return value

#         return unicode(value)

#     def value_to_string(self, obj):
#         value = self._get_val_from_obj(obj)
#         return self.get_db_prep_value(value)


# class Dummy(models.Model):
#     mylist = ListField()
