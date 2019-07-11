"""src URL Configuration

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
from todo.views import home, add_new, edit_record, remove_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_new/', add_new, name='add_new'),
    path('edit/<int:do_id>', edit_record, name='edit_record'),
    path('del/<int:do_id>', remove_record, name='remove_record'),

]
