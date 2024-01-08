from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.Login, name='login_api'),
    path('signup/',views.Signup,name='signup_api'),
    path('list/',views.Medicinelist,name='medicinelist_api'),
    path('create/',views.Medicinecreate,name='createmedicine_api'),
    path('update/<int:id>',views.Updatemedicine,name='updatemedicine_api'),
    path('delete/<int:id>',views.Deletemedicine,name='deletemedicine_api'),
    path('search/',views.Searchbar,name='search_api')
]