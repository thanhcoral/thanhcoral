
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.utils import get_time_now


class TimeSheet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    checkin = models.DateTimeField(_("check in"), default=timezone.now)
    checkout = models.DateTimeField(_("check out"), blank=True, null=True)

    late = models.IntegerField(blank=True, null=True, default=0)
    ot = models.IntegerField(blank=True, null=True, default=0)
    time = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"timesheet of user: {self.user.username} at {self.day}-{self.month}-{self.year}"

    def save(self, *args, **kwargs):
        self.year, self.month, self.day = get_time_now()
        return super().save(*args, **kwargs)


class Salary(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    month = models.IntegerField(blank=True, null=True)
    w_time = models.IntegerField(blank=True, null=True)

    salary = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"salary of user: {self.user.username} at month: {self.month}"

    def save(self, *args, **kwarngs):
        tmp, self.month, tmp = get_time_now()
        list = TimeSheet.objects.filter(user=self.user, month=self.month)
        total = 0
        for li in list:
            total += (li.time)
        self.w_time = total
        self.salary = 1.0 * (total/3600/8*500000)
        return super().save(*args, **kwarngs)




