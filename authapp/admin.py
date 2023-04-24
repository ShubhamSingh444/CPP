from django.contrib import admin

from authapp.models import Appointment, Contact,User,MembershipPlan,Enrollment,Trainer,Attendance


# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Appointment)
admin.site.register(Attendance)
admin.site.register(User)
