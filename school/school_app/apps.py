from django.apps import AppConfig

from school_app.consul import register_service


class SchoolAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school_app'

    def ready(self):
        register_service('school_service', 8002)
