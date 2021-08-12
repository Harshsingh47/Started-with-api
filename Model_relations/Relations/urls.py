"""Model_relations URL Configuration

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
from django.conf import settings
from django.urls import path,include
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home,name='home'),
    path('login_now', views.login_now,name='login_now'),
    path('wel_user',views.wel_user,name='wel_user'),
    path('log_out', views.log_out,name='log_out'),
    path('Relations/',views.post_list),
    path('Relations/<int:pk>/',views.post_detail),
    url(r'^get/$', views.UserApi.as_view({"get": "getapi"}),
        name='get_task'),
    url(r'^^post/$', views.UserApi.as_view({'post':"createapi"}),name='post_task'),
    url(r'^update1/(?P<id>[0-9]+)/$', views.UserApi.as_view({'put':"update"}),name='update_task'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.UserApi.as_view({'delete':"delete"}),name='delete_task'),

    # --------------------------------------------------------------------------------------------------------------
    # -------------------------------Many to one--------------------------------------------------------------------

    url(r'^get/data/$', views.Articleobjects.as_view({"get": "getarticle"}),
        name='get_taskss'),

    url(r'^get/post/(?P<id>[0-9]+)/$', views.Articleobjects.as_view({"post": "createaricle"}),
        name='get_data'),
    url(r'^get/update/(?P<id>[0-9]+)/$', views.Articleobjects.as_view({"put": "updatearticle"}),
        name='update_data'),
    url(r'^get/delete/(?P<id>[0-9]+)/$', views.Articleobjects.as_view({"delete": "deletearticle"}),
        name='delete_data'),
    # -----------------------------------------------------------------------------------------------------------------
    # ------------------------Many to Many-----------------------------------------------------------------------------
    url(r'^get/objects/', views.ArticleApi.as_view({"get": "getarticles"}),
        name='artice_get_data'),
    url(r'^get/post_data/(?P<id>[0-9]+)/$', views.ArticleApi.as_view({"post": "addarticles"}),
        name='artice_get_data'),
    url(r'^get/post_create_data/$', views.ArticleApi.as_view({"post": "createarticles"}),
        name='artice_create_data'),
    url(r'^get/update_article/(?P<id>[0-9]+)/$', views.ArticleApi.as_view({"put": "updatearticle"}),
        name='update_data'),
    url(r'^get/delete_article/(?P<id>[0-9]+)/$', views.ArticleApi.as_view({"delete": "deletearticles"}),
        name='delete_data'),
#     __________________________________________________________________________________________________________________



    # ---------------------------------
    url(r'^get/user_serialize/$', views.Userserializer.as_view({"get": "getuser"}),
        name='create_data'),
    url(r'^get/create_serialize/$', views.Userserializer.as_view({"post": "createuser"}),
        name='create_data'),

     url(r'^get/update_serialize/(?P<id>[0-9]+)/$', views.Userserializer.as_view({"put": "updateuser"}),
        name='update_data'),

    url(r'^get/delete_serialize/(?P<id>[0-9]+)/$', views.Userserializer.as_view({"delete": "deleteuser"}),
        name='delete_data'),

     # ----------------------------------------------------------------------------------------

     url(r'^get/serialize/$', views.Createserialize.as_view({"post": "create"}),
        name='create_data'),

    url(r'^get/serialize_update/(?P<id>[0-9]+)/$', views.Createserialize.as_view({"put": "updateworking"}),
        name='update_data'),

     url(r'^get/get_serialize/$', views.Createserialize.as_view({"get": "getallworking"}),
        name='get_data'),

    url(r'^get/serialize_delete/(?P<id>[0-9]+)/$', views.Createserialize.as_view({"delete": "deleteworking"}),
        name='delete_data'),


]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

