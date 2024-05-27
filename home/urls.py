from django.urls import path
from home import views

urlpatterns = [
    path('', views.login_form, name='login_form'),
    path('logout_manager/', views.logout_manager, name='logout_manager'),
    path('home/', views.home, name='home'),
    path('search_box/', views.search_box, name='search_box'),
    path('search_document/', views.search_document, name='search_document'),
]