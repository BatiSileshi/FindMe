from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Project(models.Model):
    owner=models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200, null=True)
    description=models.TextField(null=True)
    project_image=models.ImageField(null=True, blank=True, default="default.png")
    demo_link=models.CharField(max_length=3000, null=True, blank=True)
    source_link=models.CharField(max_length=3000, null=True, blank=True)
    tags=models.ManyToManyField('Tag', blank=True)
    review_total=models.IntegerField(default=0, null=True, blank=True)
    review_ratio=models.IntegerField(default=0, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['-review_ratio', '-review_total',  'title']
        
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True) 
        return queryset  
    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()   
        posVotes = reviews.filter(value='very_good').count()
        totalVotes= reviews.count()
        
        ratio = (posVotes / totalVotes )*100
        self.review_total = totalVotes
        self.review_ratio = ratio
        self.save()
    
    
class Review(models.Model):
    REVIEW_TYPE=(
        ('very_good', 'Positive Review'),
        ('good', 'Negative Review'),    
    )
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    body=models.TextField(null=True, blank=True)
    value=models.CharField(null=True, max_length=255, choices=REVIEW_TYPE)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    class Meta:
        unique_together = [['owner', 'project']]
    
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name=models.CharField(null=True, max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    