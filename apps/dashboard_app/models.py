from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import re
from .. login_app.models import User

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# first, last name rules    
rulesn =[lambda s: any(x.isalpha() for x in s), # must be letters      
        lambda s: len(s) > 2  and len(s) < 20,  # must be at least 2 characters
        ]

class PatientManager(models.Manager):# need to add more validations
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first_name should be at least 2 characters"
        if not all(rule(postData['first_name']) for rule in rulesn):
            errors["first_name"] = "First Name should be at least 8 characters long and should include only letters."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last_name should be at least 2 characters"
        if not all(rule(postData['last_name']) for rule in rulesn):
            errors["last_name"] = "Last Name should be at least 8 characters long and should include only letters."
        # if len(postData['sec_last_name']) < 2:
        #     errors["sec_last_name"] = "sec_last_name should be at least 2 characters"
        # if not all(rule(postData['sec_last_name']) for rule in rulesn):
        #     errors["sec_last_name"] = "Last Name should be at least 8 characters long and should include only letters."
        if not EMAIL_REGEX.match(postData['email']): 
            errors["email"]  = "Invalid email format." 

        return errors

class MedManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "name should be at least 2 characters"
        if not all(rule(postData['name']) for rule in rulesn):
            errors["name"] = "Name should be at least 8 characters long and should include only letters."
        # if len(postData['category']) < 2:
        #     errors["category"] = "category should be at least 2 characters"
        # if not all(rule(postData['category']) for rule in rulesn):
        #     errors["category"] = "category should be at least 8 characters long and should include only letters."
        if len(postData['description']) < 6:
            errors["description"] = "description should be at least 6 characters"
            
        return errors

class Patient(models.Model):    
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=255)
    sec_last_name=models.CharField(max_length=255,null=True)
    password=models.CharField(max_length=255,null=True)
    email = models.EmailField()
    address=models.TextField()
    city=models.CharField(max_length=255)
    colonia=models.CharField(max_length=255, null=True)
    state=models.CharField(max_length=255)
    zip_code=models.CharField(max_length=255)
    phone1=models.CharField(max_length=255)
    phone2=models.CharField(max_length=255,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name = "patient_creator",on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now=True)    
    objects =PatientManager()    
    # presc_meds = a list of meds prescribed to patient


class Med(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    description = models.TextField(null=True)
    presc = models.ManyToManyField(Patient, related_name="presc_meds")
    creator = models.ForeignKey(User, related_name = "meds_creator",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects =MedManager()



