from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson

class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    class Meta:
         model = Course
         fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

