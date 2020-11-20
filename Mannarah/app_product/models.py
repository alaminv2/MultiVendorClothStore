from django.db import models


class Catagory(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to="Product_imgs")
    title = models.CharField(max_length=264)
    preview_text = models.CharField(max_length=264)
    description = models.TextField(max_length=300)
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, related_name='catagory')
    price = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
