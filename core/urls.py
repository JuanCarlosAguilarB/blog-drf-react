from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Blogeros API",
      default_version='v1',
      description="API for system of blogs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [


   # login
   path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

   path('api/v1/blog/', include('apps.blog.urls')),
   path('api/v1/category/', include('apps.category.urls')),
   path('api/v1/users/', include('apps.user.urls')),
   path('api/v1/subscriptions/', include('apps.subscriptions.urls')),
   
   path('admin/', admin.site.urls),
      
   # swagger
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]