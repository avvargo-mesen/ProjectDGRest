from django.db import models

# Create your models here.

class Course(models.Model):
    name  = models.CharField (max_length =100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="users/course_images/", verbose_name="Картинка", help_text='Загрузите картинку',
                               blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name  = models.CharField (max_length =100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="users/lessons_images/", verbose_name="Картинка", help_text='Загрузите картинку',
                               blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ссылка на видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'