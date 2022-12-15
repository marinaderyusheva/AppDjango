
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


# Create your views here.
# функции для ссылок urlpatterns
def User(request):
    bd_user = User.objects.all()
    context = {
        'bd_user': bd_user
    }
    return render(request, context)


# о сервисе
def index(request):
    context = {
        'title': 'О сервисе'
    }
    return render(request, 'app1/index.html', context)


# вакансии
def vakancii(request):
    bd_vakancii = Vakancii.objects.all()  # передача из базы данных
    bd_spheres = Spheres.objects.all()
    context = {
        'bd_vakancii': bd_vakancii,
        'bd_spheres': bd_spheres,
        'title': 'Вакансии',
        'sphere_selected': 0,
    }
    return render(request, 'app1/vakancii.html', context)


# фрилансеры
def freelancer(request):
    bd_freelancer = Freelancer.objects.all()
    bd_spheres = Spheres.objects.all()
    context = {
        'bd_freelancer': bd_freelancer,
        'bd_spheres': bd_spheres,
        'title': 'Фрилансеры'

    }
    return render(request, 'app1/freelancer.html', context)


# Контакты
def contact(request):
    return render(request, 'app1/contact.html', {'title': 'Наши контакты'})


# Регистрация/вход
def registr(request):
    return render(request, 'app1/registr.html', {'title': 'Вход'})


# функция показа информации о вакансии
def show_vakancii(request, vakancii_id):
    return HttpResponse(f"Отображение вакансии с id = {vakancii_id}")


def show_sphere(request, sphere_id):
    bd_vakancii = Vakancii.objects.filter(sphere_id=sphere_id)  # фильтр по сферам
    bd_spheres = Spheres.objects.all()
    context = {
        'bd_vakancii': bd_vakancii,
        'bd_spheres': bd_spheres,
        'title': 'Отображение по сферам',
        'sphere_selected': sphere_id,
    }
    return render(request, 'app1/vakancii.html', context)


def addresume(request):
    resumeform = ResumeForm()
    if request.method == "POST":
        resumeform = ResumeForm(request.POST)
        if freelancer.is_valid():
            name = resumeform.cleaned_data["name"]
            return HttpResponse(f"<h2>Hello, {name}</h2>")
    return render(request, 'app1/addresume.html', {"form": resumeform})


def addvacancii(request):
    addvacanciiform = AddVacanciiForm()
    if request.method == "POST":
        addvacanciiform = AddVacanciiForm(request.POST)
        # if freelancer.is_valid():
        #     name = addvacanciiform.cleaned_data["name"]
        #     return HttpResponse(f"<h2>Hello, {name}</h2>")
    return render(request, 'app1/addvakancii.html', {"form": addvacanciiform})


class Add_vs(CreateView):
    form_class = AddVakancii
    template_name = 'app1/addvacancii.html'
    success_url = reverse_lazy('vakancii')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(Add_vs, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить вакансию'
        return context


# функция ошибки 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, что-то пошло не так</h1><p>Попробуйте снова</p>')
# класс представления Регистрации
# class RegistrUser(DataMixin, CreateView):
# стандартная форма джанго для регистрации пользователей
# form_class = UserCreateForm
# ссылка на шаблон
# template_name='app1/register.html'
# перенаправление на этот адрес при успешной регистрации пользователей
# success_url = reverse_lazy('login')
