from django.urls import path, re_path


from app1.views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('vakancii/', vakancii, name='vakancii'),
    path('freelancer/', freelancer, name='freelancer'),
    path('contact/', contact, name='contact'),
    # path('registr/', registr, name='registr'),
    path('addresume',addresume, name='addresume'),
    path('addvacancii',addvacancii, name='addvacancii'),
    path('addvc', vakancii, name='addvc'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('login/', login, name='login'),
    # path('vakancii/<int:vakancii_id>/', addvacancii, name='vakancii_id'),
    path('vakancii/<int:sphere_id>/', show_sphere, name='sphere_id'),
]
