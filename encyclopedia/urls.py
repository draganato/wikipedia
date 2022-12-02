from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search/', views.search, name="search"),
    path('wiki/<str:title>/', views.show, name="show"),
    path('create/', views.create_new_page, name="new_page"),
    path('rand-search/', views.rand_choose, name="rand_choose"),

]
