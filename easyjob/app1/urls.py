from django.urls import path, re_path


from app1.views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('vakancii/', vakancii, name='vakancii'),
    path('freelancer/', freelancer, name='freelancer'),
    path('contact/', contact, name='contact'),
    path('registr/', registr, name='registr'),
    path('addresume',addresume, name='addresume'),
    path('addvacancii',addvacancii, name='addvacancii'),
    #path('registr/', RegistrUser.as_view(), name='registr'),
    #path('login/', login, name='login'),
    #path('vakancii/<int:vakancii_id>/', addvacancii, name='vakancii_id'),
    path('sphere/<int:sphere_id>/', show_sphere, name='sphere_id'),
]
