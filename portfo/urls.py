from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import artifact_detail 

from . import views

urlpatterns = [
    path('search/',views.search,name='search'),
    path('artifact/<int:id>/', views.artifact_detail, name='artifact_detail'),
    path('',views.index,name='index'),
    path('comp', views.comp, name='comp'),
    path('<slug:category_slug>/<slug:slug>/',views.detail,name='post_detail'),
    path('<slug:slug>/',views.category,name='category_detail'),
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)