# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
	def validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 2:
			errors['first_name'] = "Too Short Homie!"
		if not re.match(EMAIL_REGEX, postData['email']):
			errors['email'] = "Email is janky!"
		if len(postData['password']) < 2:
			errors['password'] = "Password too short Homie!"			
		return errors
		

class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

	def __unicode__(self):
		return 'first_name: {}, last_name: {}, email: {}, password: {}, id: {}'.format(self.first_name, self.last_name, self.email, self.password, self.id)