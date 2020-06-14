from django.contrib import admin
from django.urls import path, re_path
from workspace.views import workspace, hard_sphere, soft_sphere, yukawa, dynamic_module, hard_sphere_data
from workspace.views import soft_sphere_data, yukawa_data, dynamic_data, dynamic_data_content


urlpatterns = [
    path('home', workspace, name='home_workspace'),
    re_path(r'^hard_sphere/new/$', hard_sphere, name='hard_sphere'),
    re_path(r'^soft_sphere/new/$', soft_sphere, name='soft_sphere'),
    re_path(r'^yukawa/new/$', yukawa, name='yukawa'),
    re_path(r'^dynamic_module/new/$', dynamic_module, name='dynamic_module'),
    re_path(r'^hard_sphere/data$', hard_sphere_data, name='hard_sphere_data'),
    re_path(r'^soft_sphere/data$', soft_sphere_data, name='soft_sphere_data'),
    re_path(r'^yukawa/data$', yukawa_data, name='yukawa_data'),
    re_path(r'^dynamic_module/data$', dynamic_data, name='dynamic_data'),
    path('dynamic_module/data/<directory>', dynamic_data_content, name='dynamic_data_content'),
]
