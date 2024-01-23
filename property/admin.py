from django.contrib import admin

from .models import Flat, Сomplaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ["owner", "flat"]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building',
                    'construction_year', 'town']
    inlines = [OwnerInline, ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ["liked_by"]


@admin.register(Сomplaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]
    list_display = ["text"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flats"]
    inlines = [OwnerInline, ]
    exclude = ["flats"]
