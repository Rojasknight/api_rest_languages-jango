from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('lenguagues', views.LenguagueView)
router.register('programmer', views.ProgrammerView)
router.register('paradigm', views.ParadigmView)

urlpatterns = [
    path('', include(router.urls))
]
