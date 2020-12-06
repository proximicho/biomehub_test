from django.db import models

# Create your models here.


class post(models.Model):
    post_text = models.CharField(max_length=2000)
    author = models.CharField(max_length=30)
    organism = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    modified_at = models.DateTimeField(auto_now=True)


class about(models.Model):
    about_text = models.CharField(max_length=2000)


class contact(models.Model):
    contact_text = models.CharField(max_length=2000)
