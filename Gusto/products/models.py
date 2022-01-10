from django.db import models
from django.db.models import Avg, Count
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Product table in a database
class Product(models.Model):
    title = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    ingredients = models.TextField()
    nutrition = models.TextField()
    allergens = models.TextField()
    image = models.ImageField(default='default.jpg', blank=True)
    wishlist = models.ManyToManyField(User, related_name = 'wishlist', blank = True)

    # display product title in a list of products in the table
    def __str__(self):
        return self.title

    # display first 50 characters and in the end '...', so the description
    # would be hidden for saving space purposes
    def snippet_ingr(self):
        return self.ingredients[:50] + '...'
    
    def snippet_nutr(self):
        return self.nutrition[:50] + '...'

    # count average rating for a product
    def ratingAvg(self):
        ratings = Reviews.objects.filter(product=self).aggregate(average=Avg('rating'))
        avg = 0

        if ratings['average'] is not None:
            avg = float(ratings['average'])

        return round(avg, 1)

    # count how many reviews there are for a specific product
    def reviewsCount(self):
        reviews = Reviews.objects.filter(product=self).aggregate(count=Count('id'))
        count = 0

        if reviews['count'] is not None:
            count = int(reviews['count'])

        return count

# Reviews table in the database
class Reviews(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    body = models.TextField() # review field
    date = models.DateTimeField(auto_now_add=True) # date when a review was created

    # order comments by date - from newest to oldest one
    class Meta:
        ordering = ['-date']

    # display author of a review in a list of reviews in the table    
    def __str__(self):
        return self.body # changed to body because with user it doesn't work for some reason