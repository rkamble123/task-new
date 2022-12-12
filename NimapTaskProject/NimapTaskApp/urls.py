from django.urls import path
from . import views

urlpatterns = [
    # path('log_in',views.log_in.as_view()),
    # path('log_out',views.log_out.as_view()),
    # path('user_acc',views.user_acc.as_view()),
    # path('admin_acc',views.admin_acc.as_view()),
    path('create_user',views.create_user.as_view()),
    path('create_course',views.create_course.as_view()),
    path('add_topic',views.add_topic.as_view()),
    
    

]