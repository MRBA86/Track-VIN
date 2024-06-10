from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'account'
urlpatterns=[
    path('register/', views.RegisterView.as_view() , name='register'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
