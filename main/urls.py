from main import views
from django.urls import path

app_name = 'main'
urlpatterns = [
   path('about/', views.about_page, name='about_page'),
]