import os
from celery import Celery
from django.conf import settings


# Устанавливаем переменнную DJANGO_SETTINGS_MODULE для программы командной строки Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineStore.settings')

# Создаем экземпляр приложения
app = Celery('OnlineStore')
# Загружаем настраиваемую конфигурацию из проекта
app.config_from_object('django.conf:settings')
# Celery автоматически обнаруживает асинхронные задачи
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


