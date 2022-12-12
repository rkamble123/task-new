from rest_framework import serializers
from .models import UserCreateModel , TopicsModel , CourseModel

class createUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCreateModel
        fields = '__all__'

    def create(self,valid_data):
        return UserCreateModel.objects.create(**valid_data)



class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseModel
        fields = '__all__'

    def create(self,valid_data):
        return CourseModel.objects.create(**valid_data)



class TopicSerializer(serializers.ModelSerializer):
    
    # course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = TopicsModel
        fields = '__all__'
        # read_only_fields = ('id','course_name')
        # fields = ('course_name','topic_name','topic_url')


        # category_name = serializers.RelatedField(source='category', read_only=True)

    def create(self,valid_data):
        return TopicsModel.objects.create(**valid_data)

    

 