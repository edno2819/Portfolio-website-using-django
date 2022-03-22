from django.db import models
from datetime import date, datetime





class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    tag1 = models.CharField(max_length=25, blank=True, null=True)
    tag2 = models.CharField(max_length=25, blank=True, null=True)
    tag3 = models.CharField(max_length=25, blank=True, null=True)
    link = models.CharField(max_length=2000, blank=True, null=True,)
    image = models.ImageField(upload_to="img", blank=True, null=True,)

    # @property

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=300)
    published_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class Experience(models.Model):
    designation = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_present = models.BooleanField(null=True,blank=True)
    responsibilities_1 = models.CharField(max_length=500,default=None,blank=True)
    responsibilities_2 = models.CharField(max_length=500,default=None,blank=True)
    responsibilities_3 = models.CharField(max_length=500,default=None,blank=True)
    responsibilities_4 = models.CharField(max_length=500,default=None,blank=True)
    company = models.CharField(max_length=200,default=None,blank=True)
    location = models.CharField(max_length=200,default=None,blank=True)

    def __str__(self):
        return self.designation


class Skill(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)


class Connection(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.your_name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=500)
    summary = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="img", blank=True, null=True,)
    cv = models.FileField(upload_to="cv", blank=True, null=True,)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    medium_link = models.URLField(default=None,blank=True)
    github_link = models.URLField(default=None,blank=True)
    insta_link = models.URLField(default=None,blank=True)
    linkedin_link = models.URLField(default=None,blank=True)


    def __str__(self):
        return self.name
