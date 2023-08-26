from django.contrib import admin
from .models import AssetHolder, Animal, AnimalGrade, ValuePoint, AnimalResource


class AssetHolderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user")


class AnimalAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class AnimalGradeAdmin(admin.ModelAdmin):
    list_display = ("animal", "letter_grade", "number_grade")


class ValuePointAdmin(admin.ModelAdmin):
    list_display = ("animal_grade", "date", "price")


class AnimalResourceAdmin(admin.ModelAdmin):
    list_display = ("owner", "type", "price", "weight")


# Register the admin classes
admin.site.register(AssetHolder, AssetHolderAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalGrade, AnimalGradeAdmin)
admin.site.register(ValuePoint, ValuePointAdmin)
admin.site.register(AnimalResource, AnimalResourceAdmin)
