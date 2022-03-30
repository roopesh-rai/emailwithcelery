# from __future__ import absolute_import, unicode_literals
# import os
# # from .celery import app as celery_app
# from celery import Celery
# from django.conf import settings
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')
#
# app = Celery('django_celery_project')
# app.conf.enable_utc = False
#
# app.conf.update(timezone='Asia/Kolkata')
#
# # app.config_from_object(settings, namespace='CELERY')
# app.config_from_object(settings)
#
# # Celery Beat Settings
#
# app.autodiscover_tasks(settings.INSTALLED_APPS)
#
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))