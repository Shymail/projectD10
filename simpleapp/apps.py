from django.apps import AppConfig


class SimpleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'

    def ready(self):
        from .signals import send_notifications, notify_about_new_post

red = redis.Redis(
    host='redis-10432.c1.us-central1-2.gce.cloud.redislabs.com:',
    port=10432,
    password='mrmzcGuyKz5NrEFAYZljMK2GOEK5Jthy'
)