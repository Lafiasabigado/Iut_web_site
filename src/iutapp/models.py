from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Contact(models.Model):
    slug = models.SlugField(verbose_name='Id',unique=True ,blank=True)
    lastname = models.CharField(max_length=300, unique=True, verbose_name='Nom')
    surname = models.CharField(max_length=300, unique=True, verbose_name='Prénoms')
    email = models.EmailField(unique=True,verbose_name='Email')
    date_post = models.DateTimeField(blank=True,auto_now=True,verbose_name='Date de Post')
    date_of_birthday = models.DateField(blank=True,null=True,verbose_name="Date de naissance")
    content = models.TextField(verbose_name='Message')

    class Meta:
        ordering = ["-date_post"]
        verbose_name = "Information"

    def __str__(self):
        return self.surname

    def save(self, *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.surname)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('iutapp:create')

class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='iut/')
    qualite = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
