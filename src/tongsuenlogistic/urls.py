"""tongsuenlogistic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from products.views import ProductListView, ProductDetailView

from .views import home_page,contact_page,about_page,email,change_lang_to_thai,change_lang_to_eng,change_lang_to_cn
urlpatterns = [
    path('', home_page,name="home"),
    path('about/', contact_page),
    path('contact/', contact_page),
    path('email/', email),
    path('th/', change_lang_to_thai,name="th"),
    path('en/', change_lang_to_eng,name="en"),
    path('cn/', change_lang_to_cn,name="cn"),
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
