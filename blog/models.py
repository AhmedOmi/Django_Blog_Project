from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class article(models.Model):
    Name = models.CharField(unique=True, max_length=255)
    Company = models.CharField(max_length=255, default="Company")
    Website = models.URLField()
    Linkedin = models.URLField()
    Email = models.CharField(unique=True, max_length=255)
    Photo = models.ImageField(blank=True, upload_to='images/')
    Text = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)
    Update_on = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(choices=STATUS, default=0)
    Author = models.ForeignKey(User, on_delete=models.CASCADE,  default="Author")

    def __str__(self):
        return self.Name
