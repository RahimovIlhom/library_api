from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from library.views import BookListApiView


router = DefaultRouter()
router.register(r'books', BookListApiView, basename='books')

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="Library buy",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="ilhomjon@mail.ru"),
        license=openapi.License(name="Library License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include('library.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/register/', include('dj_rest_auth.registration.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
