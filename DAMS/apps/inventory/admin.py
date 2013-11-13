from django.contrib import admin

from DAMS.apps.inventory.models import ItemTemplate, Log, \
                             Inventory, Location, Supplier


class ItemTemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('supplies', 'suppliers')


admin.site.register(Location)
admin.site.register(Log)
admin.site.register(ItemTemplate, ItemTemplateAdmin)
admin.site.register(Inventory)
admin.site.register(Supplier)


