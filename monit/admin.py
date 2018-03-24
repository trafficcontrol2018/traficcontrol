from django.contrib import admin
from monit.models import LogDataMonit,LogErrorMonit

admin.site.register(LogDataMonit)
admin.site.register(LogErrorMonit)

