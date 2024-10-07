"""
URL configuration for sim_card project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from input import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.useraction, name='useraction'),
    path('activate/', views.activate_sim, name='activate_sim'),  
    path('deactivate/', views.deactivate_sim, name='deactivate_sim'),  
    path('sim-details/<str:sim_number>/', views.get_sim_details, name='get_sim_details'), 
    path('activate-page/', views.activate_sim_page, name='activate_sim_page'),
    path('deactivate-page/', views.deactivate_sim_page, name='deactivate_sim_page'),
    path('get-sim-details-page/', views.get_sim_details_page, name='get_sim_details_page'),
]



