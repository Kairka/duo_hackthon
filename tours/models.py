from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, primary_key=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tour(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tours_image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='tours')
    date = models.DateField()

    def __str__(self):
        return self.name



