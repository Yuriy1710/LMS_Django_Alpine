from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, related_name="courses", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name