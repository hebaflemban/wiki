from django.db import models
from django.urls import reverse

# Create your models here.

class Page(models.Model):
    title = models.CharField (max_length = 50)
    content = models.TextField()
    last_update = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.title



    #Page.get_absolute_url()

    def get_absolute_url (self):
        #   return reverse('pages.views.detail', args=[str(self.id)])
        return reverse('page-detail', args =[str(self.id)])
