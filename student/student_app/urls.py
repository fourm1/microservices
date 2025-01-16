from django.http import JsonResponse
from django.urls import include, path
from rest_framework import routers

from student_app.views import StudentViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet)

def health_check(request):
    return JsonResponse({'status': 'healthy'})

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check),
]