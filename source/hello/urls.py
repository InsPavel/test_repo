"""hello URL Configuration

    path('articles/add/', webapp_views.article_create_view),
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from webapp import views as webapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp_views.index_view, name='index'),
    path('articles/', webapp_views.article_list, name='article_list'),
    path('article/<int:pk>/', webapp_views.article_view, name='article_view'),
    path('articles/add/', webapp_views.article_create_view, name='article_add'),
    path('issues/', webapp_views.issue_list, name='issue_list'),
    path('issue/<int:pk>/', webapp_views.issue_view, name='issue_view'),
    path('issues/add/', webapp_views.issue_create_view, name='issue_add'),
    path('issue/delete/', webapp_views.issue_delete_view),
    path('issue/<int:pk>/edit/', webapp_views.issue_update_view, name='issue_update'),
    path('issue/delete/get/', webapp_views.issue_get_delete, name='issue_delete_all'),
    path('issue/delete/post/', webapp_views.issue_post_delete, name='issue_delete_post'),
]
