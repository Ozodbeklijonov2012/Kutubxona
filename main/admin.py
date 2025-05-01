from django.contrib import admin
from .models import *

admin.site.register(Talaba)
admin.site.register(Muallif)
admin.site.register(Kitob)
admin.site.register(Admin)
admin.site.register(Record)


admin.site.register(
    [
        Xarid, Kurs, Profil, Tanlangan, Izoh, Student, Universitet, Yonalish, Ustoz,
    ]
)
