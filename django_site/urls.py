"""
URL configuration for django_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
                  path('', include('base.urls')),
                  path('admin/', admin.site.urls),
                  path('user/', include('user.urls')),
                  path('product/', include('product.urls')),
                  path('cart/', include('cart.urls')),
                  path('payment/', include('payment.urls')),
                  path('order/', include('order.urls')),
                  path('JWT/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('JWT/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
              ] + static(settings.MEDIA_URL, documect_root=settings.MEDIA_ROOT)
