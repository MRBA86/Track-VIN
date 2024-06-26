from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
app_name = 'home'
urlpatterns=[
    path('',views.HomeView.as_view(), name = 'home')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)