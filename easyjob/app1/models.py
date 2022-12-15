from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
#таблица вакансий
class Vakancii(models.Model):
    title_vakancii = models.CharField(max_length=255, verbose_name='Наименование вакансии')
    rabotodat = models.ForeignKey('Rabotodateli', on_delete=models.PROTECT)
    sphere = models.ForeignKey('Spheres', on_delete=models.PROTECT)
    about_vakancii = models.TextField(blank=True, verbose_name='О вакансии')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    is_published = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return self.title_vakancii

    def get_absolute_url(self):
        return reverse('vakancii', kwargs={'vakancii_id': self.id})

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'
        ordering = ['sphere', 'time_create']

#таблица фрилансеров
class Freelancer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    sphere = models.ForeignKey('Spheres', on_delete=models.PROTECT)
    age = models.IntegerField(null=True, verbose_name='Возраст')
    experience = models.IntegerField(null=True, verbose_name='Опыт работы')
    about_freelancer = models.TextField(blank=True, verbose_name='О себе')
    vakancii = models.ForeignKey('Vakancii', on_delete=models.PROTECT)

    def __str__(self):
        return self.about_freelancer

    class Meta:
        verbose_name = 'Фрилансеры'
        verbose_name_plural = 'Фрилансеры'
        ordering = ['sphere', 'experience'] #сортировка

#таблица сфер деятельности
class Spheres(models.Model):
    SPHERE_CHOICES=[
        ('D', 'Дизайн'),
        ('M', 'Маркетинг'),
        ('P', 'Программирование'),
    ]

    name_sphere = models.CharField(max_length=10, choices=SPHERE_CHOICES, default='D')

    #метод класса, возвращает удобночитаемое имя
    def __str__(self):
        return self.name_sphere

    def get_absolute_url(self):
        return reverse('sphere', kwargs={'sphere_id': self.id})

    class Meta:
        verbose_name = 'Cферы'
        verbose_name_plural = 'Cферы'
        ordering = ['name_sphere']  # сортировка

#таблица работодателей
class Rabotodateli(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    period_onsite = models.DateField(null=True, verbose_name='На сайте с ')
    is_company = models.BooleanField(default=False, verbose_name='Человек/Компания')

    class Meta:
        verbose_name = 'Работодатели'
        verbose_name_plural = 'Работодатели'
        ordering = ['is_company']  # сортировка





