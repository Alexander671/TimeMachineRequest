from django_cron import CronJobBase, Schedule
from django.core.files import File
from django.utils import timezone, dateformat
from .models import Request
from requests import get
def printHello():
    now = timezone.now().replace(second=0, microsecond=0)
    print(now)
    req = list(Request.objects.filter(time_request=now))
    print(req)
    ###############################################


    for i in range(len(req)):
        req[i].response = (get(req[i].url)).ok
    print(req)
    Request.objects.bulk_update(req, ["response"])
    ###############################################

