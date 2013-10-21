import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as __init__

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Poll")
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choise(models.Model):
    poll = models.ForeignKey(Poll)
    choice_texr = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice
