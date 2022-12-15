from django.contrib import admin
from .models import *
# Register your models here.

class VakanciiAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_vakancii', 'about_vakancii', 'time_create','time_update','is_published')
    list_display_links = ('id', 'title_vakancii')
    search_fields = ('title_vakancii', 'about_vakancii')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')

class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('id','age', 'experience', 'about_freelancer')
    list_display_links = ('id','about_freelancer')
    search_fields = ('id',)

class SpheresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_sphere',)
    list_display_links = ('name_sphere',)
    search_fields = ('name_sphere',)

class RabotodateliAdmin(admin.ModelAdmin):
    list_display = ('id', 'period_onsite', 'is_company')
    list_display_links = ('id',)
    search_fields = ('id',)

admin.site.register(Vakancii, VakanciiAdmin)
admin.site.register(Freelancer, FreelancerAdmin)
admin.site.register(Spheres, SpheresAdmin)
admin.site.register(Rabotodateli, RabotodateliAdmin)