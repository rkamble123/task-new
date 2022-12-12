from django.contrib import admin
from .models import CourseModel,TopicsModel,UserCreateModel

# Register your models here.

admin.site.register(UserCreateModel)

@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name']


@admin.register(TopicsModel)
class TopicModel(admin.ModelAdmin):
    list_display = ['course_name','topic_name','topic_url']



