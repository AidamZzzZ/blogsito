from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.title