from django.contrib import admin
from .models import Car, CarModel, Company, CarColor
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "vin_number",
        "car_model",
        "company",
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "vin_number", "color"), "image"
            )
        }),
        ('Advanced options', {
            'fields': ("car_model", "company"),
        }),
    )
    readonly_fields = [
        "company"
    ]

class CarInline(admin.StackedInline):
    model = Car

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
    inlines = [
        CarInline,
    ]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
