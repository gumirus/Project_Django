"""
URL configuration for Site project.

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
from App.views import index_view, page2_view, game_page_view, game_view, link_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),  # Главная страница
    path('page2/', page2_view, name='page2'),  # Вторая страница
    path('game_page/', game_page_view, name='game_page'),  # Страница игры
    path('game/', game_view, name='game'),  # Маршрут для игры
    path('link/', link_view, name='link'),  # Страница с ссылкой (если нужно)
]

