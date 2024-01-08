from django.contrib import admin
from .models import Medicines

# Register your models here.
class MedicineList(admin.ModelAdmin):
    list_display=['name','company','price','dosage']

admin.site.register(Medicines,MedicineList)