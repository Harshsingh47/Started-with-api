"""Rest_framework URL Configuration

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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

        url(r'^get/user_data/$', views.Createposts.as_view({"get": "getpost"}),
                name='get_user_post'),

        url(r'^get/get_create_data/$', views.Createposts.as_view({"post": "createdata"}),
                name='get_user_post_id'),

        url(r'^get/get_update_data/(?P<id>[0-9]+)/$', views.Createposts.as_view({"put": "updateposts"}),
                name='get_user_post_update'),

        url(r'^get/get_delete_data/(?P<id>[0-9]+)/$', views.Createposts.as_view({"delete": "deleteposts"}),
                name='get_user_post_delete'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
