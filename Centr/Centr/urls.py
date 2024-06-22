from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('catalog/<str:type>/<int:id>/', views.product_detail, name='product_detail'),
    path('production/', views.production_view, name='production'),
    path('directory/', views.directory_view, name='directory'),
    path('directory/auto', views.auto_view, name='auto'),
    path('directory/aviation', views.aviation_view, name='aviation'),
    path('directory/cable', views.cable_view, name='cable'),
    path('directory/conservation', views.conservation_view, name='conservation'),
    path('directory/multi', views.multi_view, name='multi'),
    path('directory/lowtemp', views.lowtemp_view, name='lowtemp'),
    path('directory/instrumentation', views.instrumentation_view, name='instrumentation'),
    path('directory/gearbox', views.gearbox_view, name='gearbox'),
    path('directory/reinforcing', views.reinforcing_view, name='reinforcing'),
    path('directory/conductive', views.conductive_view, name='conductive'),
    path('directory/lithium', views.lithium_view, name='lithium'),
    path('map/', views.map_view, name='map'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('contact/', views.FeedBackView.as_view(), name='contact')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Main.views.custom_404'