from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 50, null=False, blank=False,primary_key = True,default = 'default')
    firstname = models.CharField(max_length = 50, null=True, blank=True)
    middlename = models.CharField(max_length = 50, null=True, blank=True)
    lastname = models.CharField(max_length = 50, null=True, blank=True)
    password = models.CharField(max_length = 50, null=True, blank=True)
    emailAddress = models.CharField(max_length = 50, null=True, blank=True)
    gender = models.CharField(max_length = 50, null=True, blank=True)
    birthdate = models.DateField(default = datetime.now(), null=True, blank=True)
    class Meta:
        db_table = "User"
    
class UserRequest(models.Model):
    requestID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,max_length = 50, null = False, blank = False, on_delete = models.CASCADE, related_name = "userID")
    isApprove = models.IntegerField()
    class Meta:
        db_table = "UserRequest"

class Organizer(models.Model):
    organizerID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,max_length = 50, null = False, blank = False, on_delete = models.CASCADE, related_name = "organizerUser")
    class Meta:
        db_table = "Organizer"