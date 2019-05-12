"""myproject URL Configuration

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
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='home'),
    path('myapp/<int:board_id>/', myapp.views.detail, name="detail"),
    path('myapp/new/', myapp.views.new, name="new"),
    path('myapp/create/', myapp.views.create, name="create"),
    path('myapp/delete/<int:board_id>', myapp.views.delete, name="delete"),
    path('myapp/edit/<int:board_id>', myapp.views.edit, name="edit"),
    path('myapp/update/<int:board_id>', myapp.views.update, name="update"),
    path('myapp/<int:board_id>/comments/new', myapp.views.comment_new, name="comment_new"),
    path('myapp/<int:board_id>/comments/<int:comment_id>/delete',myapp.views.comment_delete, name="comment_delete"),
]
