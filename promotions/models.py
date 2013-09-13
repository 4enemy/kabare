from django.db import models

class Promo(models.Model):
    posting_date = models.DateTimeField(auto_now_add = True)
    header = models.CharField(max_length=200)
    text = models.TextField()
    
    def __unicode__(self):
        return self.header

