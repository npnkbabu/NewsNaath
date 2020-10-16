from django.db import models

# Create your models here.
class Source(models.Model):
    source_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField()
    
    def __str__(self):
        return self.name



class Source_Details(models.Model):
    source_details_id = models.IntegerField(primary_key=True)
    source_id = models.ForeignKey(Source,on_delete=models.CASCADE)
    rss_feed_url = models.CharField(max_length=500)
    
    def __str__(self):
        return self.rss_feed_url



class News_type(models.Model):
    news_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class News_data(models.Model):
    news_data_id = models.IntegerField(primary_key=True)
    source_id = models.ForeignKey(Source,on_delete=models.CASCADE)
    news_type_id = models.ForeignKey(News_type,on_delete=models.CASCADE)
    news_date = models.DateField()
    news_data = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.news_data_id)



class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    news_data_id = models.ForeignKey(News_data,on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    article_data = models.TextField()
    
    def __str__(self):
        return str(self.article_id)


