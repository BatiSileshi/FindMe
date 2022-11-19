from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200, null=True)
    description=models.TextField(null=True)
    project_image=models.ImageField(null=True, blank=True, default="default.png")
    demo_link=models.CharField(max_length=3000, null=True, blank=True)
    source_link=models.CharField(max_length=3000, null=True, blank=True)
    tags=models.ManyToManyField('Tag', blank=True)
    review_total=models.IntegerField(default=0, null=True)
    review_ratio=models.IntegerField(default=0, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    REVIEW_TYPE=(
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('bad', 'Bad'),
    )
    # owner=
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    body=models.TextField(null=True, blank=True)
    value=models.CharField(null=True, max_length=255, choices=REVIEW_TYPE)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name=models.CharField(null=True, max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    