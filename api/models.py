from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
	phone=models.CharField(max_length=256, blank=True, null=True)
	u_id=models.AutoField(primary_key=True)
	oauth=models.CharField(max_length=20,blank=True,null=True)
	class Meta:
		db_table = 'user'

class GCM(models.Model):
	u_id=models.IntegerField(blank=True,primary_key=True) 
	regid=models.CharField(max_length=256,blank=256, null=True)    
	class Meta:
		db_table="gcm"

class Family(models.Model):
	phone=models.CharField(max_length=256, blank=True, null=True)	
	class Meta:
		db_table="family"


class Friend(models.Model):
	phone=models.CharField(max_length=256, blank=True, null=True)	
	class Meta:
		db_table="friend"


class Other(models.Model):
	phone=models.CharField(max_length=256, blank=True, null=True)	
	class Meta:
		db_table="other"					   