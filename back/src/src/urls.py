
from django.contrib import admin
from django.urls import include, path , re_path
from rest_framework import routers
from articles import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('articles.api.urls')),
    re_path('.*',TemplateView.as_view(template_name='index.html'))
]