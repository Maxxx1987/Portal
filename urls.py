"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from apps.categories.views import CategoryListView, TopicListView, TopicCreateView, RegisterUser, LoginUser, logout_user
from apps.comments.views import CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView
from apps.votes.views import VoteCreateView, VoteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    #path('accounts/', include('allauth.urls')),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<str:assign>/', TopicListView.as_view()),
    path('categories/<str:assign>/add_topic/', TopicCreateView.as_view()),

    path('categories/<str:assign>/topics/<str:slug>/', CommentListView.as_view()),
    path('categories/<str:assign>/topics/<str:slug>/add_comment/', CommentCreateView.as_view()),
    path('categories/<str:assign>/topics/<str:slug>/comments/<int:pk>/update/', CommentUpdateView.as_view()),
    path('categories/<str:assign>/topics/<str:slug>/comments/<int:pk>/delete/', CommentDeleteView.as_view()),

    path('categories/<str:assign>/topics/<str:slug>/comments/<int:pk>/vote/', VoteCreateView.as_view()),
    path('categories/<str:assign>/topics/<str:slug>/comments/<int:pk>/vote/<int:vote_id>/delete/', VoteDeleteView.as_view()),
]
