"""shortneturl URL Configuration

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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from shorter import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__dubug__/", include(debug_toolbar.urls)),
    path("", views.index, name = "index"),
    path("get_user/<int:user_id>", views.get_user),
    path("register", views.register_view, name = "register"),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path("list_view", views.list_view, name='list'),
]
