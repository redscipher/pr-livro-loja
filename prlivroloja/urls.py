"""
URL configuration for prlivroloja project.

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

#== importacoes
#django
from django.contrib import admin
from django.urls import path, re_path, include
#debug
from debug_toolbar.toolbar import debug_toolbar_urls
#rest framework
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    #parametros regulares
    re_path('livroloja/(?P<versao>(v1|v2))/', include('ordem.urls')),
    re_path('livroloja/(?P<versao>(v1|v2))/', include('produto.urls')),
    path('api-token/', obtain_auth_token, name='api_token')
]  + debug_toolbar_urls()
