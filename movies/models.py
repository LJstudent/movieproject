from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_title = models.CharField(max_length=200, null=False, blank=False)
    pub_date = models.DateTimeField('date published')
    rating = models.DecimalField(max_digits=20, decimal_places=2)
    def __str__(self):
        return self.movie_title
   