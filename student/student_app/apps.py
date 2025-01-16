from django.apps import AppConfig

from student_app.consul import register_service


class StudentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_app'

    def ready(self):
        register_service('student_service', 8001)
