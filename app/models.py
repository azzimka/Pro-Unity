from django.db import models
from django.urls import reverse
from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('category_detail_url',kwargs={'slug':self.slug})


class Course(models.Model):
    image = models.ImageField(upload_to='courses/')
    # ----------------
    title = models.CharField(max_length=255)
    # -------------------

    profession = models.CharField(max_length=100, null=True)

    
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)


    def __str__(self):
        return self.profession
    

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug})








class Registration(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    it = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)


    def __str__(self):
        return self.ism
    
