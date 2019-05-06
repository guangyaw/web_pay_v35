"""web_pay_v35 URL Configuration

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

from pay_info.views import testutl,step1url,step2url,step3url,step4url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', testutl),
    path('step1/', step1url),
    path('step2/', step2url),
    path('step3/', step3url),
    path('step4/', step4url),
]
