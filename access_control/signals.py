import subprocess
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import AccessLog

LOG_FILE = "system_events.log"


@receiver(post_save, sender=AccessLog)
def log_access_create(sender, instance, created, **kwargs):
    if created:
        status = "GRANTED" if instance.access_granted else "DENIED"
        message = f"[{now()}] - CREATE: Access log created for card {instance.card_id}. Status: {status}.\n"
        subprocess.run(f'echo "{message}" >> {LOG_FILE}', shell=True)


@receiver(post_delete, sender=AccessLog)
def log_access_delete(sender, instance, **kwargs):
    message = f"[{now()}] - DELETE: Access log (ID: {instance.id}) for card {instance.card_id} was deleted.\n"
    subprocess.run(f'echo "{message}" >> {LOG_FILE}', shell=True)
