from django.db import models


class EnergyInsight(models.Model):
    end_year = models.CharField(max_length=10, blank=True, null=True)
    intensity = models.IntegerField(default=0)
    sector = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    insight = models.TextField()
    url = models.URLField(max_length=500)
    region = models.CharField(max_length=200)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    impact = models.CharField(max_length=50, blank=True, null=True)
    added = models.CharField(max_length=50)
    published = models.CharField(max_length=50)
    country = models.CharField(max_length=200)
    relevance = models.IntegerField(default=0)
    pestle = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    likelihood = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
