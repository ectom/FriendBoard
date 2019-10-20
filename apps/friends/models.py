from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 3:
            errors['name'] = "Name must be at least 3 characters long"
        if len(post_data['alias']) < 3:
            errors['alias'] = "alias must be at least 3 characters long"
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "Email must be of correct format."
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if post_data['password'] != post_data['confirm']:
            errors['password'] = "Password must match password confirmation field"
        if post_data['birthday'] == None:
            error['birthday'] = 'Cannot leave date of birth blank'
        print(errors)
        return errors
    def adds(self, user_id, friend):
        user = self.get(id=user_id)
        the_friend = self.get(id=friend)
        Friend.objects.create(users=user, friends=the_friend)
        Friend.objects.create(users=the_friend, friends=user)

    def removes(self, user_id, friend):
        user = self.get(id=user_id)
        the_friend = self.get(id=friend)
        first = Friend.objects.get(users=user, friends=the_friend)
        first.delete()
        second = Friend.objects.get(users=the_friend, friends=user)
        second.delete()

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    objects = UserManager()
    def __repr__(self):
        return "{}, {}".format(self.name, self.alias)

class Friend(models.Model):
    name = models.CharField(max_length=255)
    users = models.ForeignKey(User, related_name='request', on_delete=models.PROTECT)
    friends = models.ForeignKey(User, related_name='accept', on_delete=models.PROTECT)
    def __repr__(self):
        return "{}, {}".format(self.users, self.friends)
