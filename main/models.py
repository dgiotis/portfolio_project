from django.db import models

# Here im creating the Models of the Project that ill need to pass dta dynamicly to db. 
class Project(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200, blank=True) #todo: make a seperate model for adding tech stack.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)  # e.g., 0-100%
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
