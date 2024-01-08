"""Medicalshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from medapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('medapp/', include('medapp.urls')),
    path('signup/',views.Signup,name='signup'),
    path('',views.LoginPage,name='login'),
    path('base/',views.Homepage,name='base'),
    path('logout/',views.LogoutPage,name='logout'),
    path('meds/',views.Meds,name='meds'),
    path('delete/<int:id>',views.Delete_record,name='delete'),
    path('<int:id>',views.Update_record,name='update'),
    path('add/',views.Add,name='add'),
    path('search/',views.Searchbar,name='search'),
    path('medapi/',include('medapi.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
