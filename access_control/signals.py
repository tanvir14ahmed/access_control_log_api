import subprocess
import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from django.conf import settings
from .models import AccessLog

# Absolute path to log file (Windows safe)
LOG_FILE = os.path.join(settings.BASE_DIR, "system_events.log")


def write_log_windows(message: str):
    """
    Writes log using Windows cmd safely
    """
    command = f'cmd /c echo {message}>>"{LOG_FILE}"'
    subprocess.run(command, shell=True)


@receiver(post_save, sender=AccessLog)
def log_access_create(sender, instance, created, **kwargs):
    if created:
        status = "GRANTED" if instance.access_granted else "DENIED"
        message = f"[{now().strftime('%Y-%m-%d %H:%M:%S')}] - CREATE: Access log created for card {instance.card_id}. Status: {status}."
        write_log_windows(message)


@receiver(post_delete, sender=AccessLog)
def log_access_delete(sender, instance, **kwargs):
    message = f"[{now().strftime('%Y-%m-%d %H:%M:%S')}] - DELETE: Access log (ID: {instance.id}) for card {instance.card_id} was deleted."
    write_log_windows(message)
