from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank = True, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    featured_image = models.ImageField(null = True, blank = True, default ="default.jpg")
    demo_link = models.CharField(max_length=2000, null = True, blank = True)
    source_link = models.CharField(max_length=2000, null = True, blank = True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
      return  self.title


    class Meta:
        ordering = ['-vote_ratio', 'vote_total', 'title']


    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    

    # THIS BLOCK OF CODES COLLECTS ALL THE USERS AND NEVER ALLOWS USERS TO VOTE OR RATE ITSELF
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    # THIS BLOCK OF CODES CALCULATE THE NUMBER OF VOTES AND REVIEW PERCENTAGE
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()




    
        

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=CASCADE)
    body = models.TextField(null = True, blank = True)
    value = models.CharField(max_length = 200, choices= VOTE_TYPE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value

#the tag here stands for verified agents. anywhere "tag" is seen is for agents

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    

    def __str__(self):
        return self.name


        

