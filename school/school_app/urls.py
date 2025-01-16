from django.http import JsonResponse
from django.urls import include, path
from rest_framework import routers

from school_app import views

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet)

def health_check(request):
    return JsonResponse({'status': 'healthy'})

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check),
]