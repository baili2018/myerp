"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from erp import views
from django.conf.urls.static import static
from cms import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cost/$', views.cost_list, name='costlist'),
    url(r'^cost/add/$', views.cost_add, name='costadd'),
    url(r'^$', views.index, name='index'),
    url(r'^index?v=3$', views.index3, name='index3'),
    url(r'^tem/$', views.tem, name='tem'),
    url(r'^product/$', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
