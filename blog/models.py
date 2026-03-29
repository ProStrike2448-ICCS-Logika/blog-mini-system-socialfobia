from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256 , unique=True)
    content = models.TextField()
    published_date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.published_date}: {self.title}"
    
    

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']
class Author(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name