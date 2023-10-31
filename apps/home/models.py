# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta

ATTENDANCE_STATUS = (
    ("PRESENT", "present"),
    ("ABSENT", "absent"),
    ("LEAVE", "leave"),
)


class ZoomParticipant(models.Model):
    participant_id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    date = models.DateField(auto_now=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    attendance_status = models.CharField(max_length=9,
                             choices=ATTENDANCE_STATUS,
                             default="PRESENT")

    def __str__(self):
        return self.name
    #
    # def save(self, *args, **kwargs):
    #     if self.join_time and self.leave_time:
    #         # Calculate the duration
    #         duration = self.leave_time - self.join_time
    #
    #         # Store the duration in the Time_duration field
    #         self.duration = duration
    #
    #     super(ZoomParticipant, self).save(*args, **kwargs)
