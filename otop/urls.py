from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from index import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path('hello/', views.hello, name='home'),
    path('', views.index, name='index'),
    path('2', views.home2, name='page2'),
    path('3', views.home3, name='page3'),
    path('4', views.home4, name='page4'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
