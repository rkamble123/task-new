from django.db import models

# Create your models here.

class UserCreateModel(models.Model):

    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update_date = models.DateField(blank=True,null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def validate_password(self,value):
        pass


class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class TopicsModel(models.Model):
    course_name = models.ForeignKey(CourseModel,on_delete=models.DO_NOTHING)
    topic_name = models.CharField(max_length=100)
    topic_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.course_name} {self.topic_name}'