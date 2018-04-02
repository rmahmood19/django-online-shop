import os
import random
from django.db import models
from django.utils.text import slugify

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name , ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,60000)
    product_folder  = instance.id
    name,ext = get_filename_ext(filename)
    final_filename = "{new_filename}.{ext}".format(new_filename=new_filename,ext=ext)
    return "products/{product_folder}/{final_filename}".format(product_folder=product_folder,
                                                            final_filename=final_filename)

class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None
    def featured(self):
        return self.get_queryset().filter(featured=True)

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=120)
   
    description = models.TextField()
    slug        = models.SlugField(max_length=200, unique=True,blank=True, null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=12,default=10.00)
    image       = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    featured    = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        num = random.randint(1,90000)
        unique_slug = '{}-{}'.format(slug, num)
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    
    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

