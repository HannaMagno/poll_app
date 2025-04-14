from django.db import models
from django.urls import reverse

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse('poll_detail', args=[str(self.id)])
    
    def total_votes(self):
        return sum(choice.votes for choice in self.choices.all())
    
    class Meta:
        ordering = ['-pub_date']

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text