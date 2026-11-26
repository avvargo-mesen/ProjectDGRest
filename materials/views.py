from django.shortcuts import render
from rest_framework import generics, viewsets
from materials.serializers import CourseSerializer, LessonSerializer
from materials.models import Course, Lesson
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModer

# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
         if self.action in ['create', 'destroy']:
             self.permission_classes = [IsAuthenticated, ~IsModer]
         elif self.action in ['list', 'retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated]
         return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

