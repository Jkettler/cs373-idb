from django.contrib import admin
from idb.models import Senator, Committee, Bill, Vote

admin.site.register(Senator)
admin.site.register(Committee)
admin.site.register(Bill)
admin.site.register(Vote)