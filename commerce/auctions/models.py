from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    pass

class Listings(models.Model):

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    startingBid = models.IntegerField()
    listingImage = models.CharField(max_length = 4096)
    datePosted = models.DateField(default=datetime.datetime.now())
    #lister = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}"

class Bids(models.Model):
    bid = models.IntegerField()
    bidder = models.ForeignKey(User,on_delete=models.CASCADE)
    bidOn = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bids")
class Comments(models.Model):
    comment = models.CharField(max_length=1024)
    commentBy = models.ForeignKey(User, on_delete=models.CASCADE)
    commentOn = models.ForeignKey(Listings, on_delete=models.CASCADE,related_name="comments")
