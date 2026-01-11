"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views
from app.routers import router
urlpatterns =[

    # Function Based
    path('fbv/movies/', views.fbv_movie_list),
    path('fbv/movies/<int:pk>/', views.fbv_movie_detail),

    # Class Based
    path('cbv/movies/', views.CBVMovie.as_view()),
    path('cbv/movies/<int:pk>/', views.CBVMovieDetail.as_view()),

    # Mixins
    path('mixin/movies/', views.MixinMovieList.as_view()),
    path('mixin/movies/<int:pk>/', views.MixinMovieDetail.as_view()),

    # Generic
    path('generic/movies/', views.GenericMovieList.as_view()),
    path('generic/movies/<int:pk>/', views.GenericMovieDetail.as_view()),

    # ViewSet
    path('', include(router.urls)),
    
]

