from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('app1/', include('app.urls')),
    path('app2/', include('app2.urls')),
]