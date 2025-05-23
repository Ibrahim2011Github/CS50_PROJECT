from django.db import models
from django.urls import reverse

# Create your models here.def 


class Italy(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    p = models.CharField(max_length=100, null=True, blank=True)
    content2 = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
      return reverse('post', kwargs={'post_id': self.pk})
  
    
  
    class Meta:
        verbose_name = 'Italy'
        verbose_name_plural = 'Italy'
        ordering = ['-time_create', 'title']
    

class Category (models.Model):
    name = models.CharField(max_length=55, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
      return reverse('category', kwargs={'cat_id': self.pk})
  
    