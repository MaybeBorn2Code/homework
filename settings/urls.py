# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# DRF
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from store.views import MainViewSet


router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('main', MainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
