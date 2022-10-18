from django.contrib import admin

from . import models


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Actor._meta.fields]
    search_fields = ('first_name', 'last_name',)
    search_help_text = 'Search by first name and last name'
    empty_value_display = '-'
    ordering = ('last_name', 'first_name',)
    list_per_page = 25


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Address._meta.fields]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Category._meta.fields]


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.City._meta.fields]


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Country._meta.fields]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Customer._meta.fields]


@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Film._meta.fields]


@admin.register(models.FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.FilmActor._meta.fields]


@admin.register(models.FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.FilmCategory._meta.fields]


@admin.register(models.Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Inventory._meta.fields]


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Language._meta.fields]


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Payment._meta.fields]


@admin.register(models.Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Rental._meta.fields]


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Staff._meta.fields]


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Store._meta.fields]