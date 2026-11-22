from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Course, Lesson

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=35, verbose_name="Телефон", help_text='Введите номер', blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", help_text='Загрузите картинку',
                               blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Payments(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ("cash", "Наличные"),
        ("transfer", "Перевод на счет"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name="Оплаченный курс", blank=True, null=True)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", blank=True, null=True)
    sum = models.PositiveIntegerField()
    payment_way = models.CharField(max_length=20,choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return str(self.payment_date)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


