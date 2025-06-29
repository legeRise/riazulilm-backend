from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages = models.IntegerField()
    cover_image = models.URLField(blank=True, null=True)
    download_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def formatted_date(self):
        return self.published_date.strftime('%B %d, %Y')