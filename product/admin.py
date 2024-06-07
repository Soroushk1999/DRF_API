from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('low', 'Low (< $100)'),
            ('medium', 'Medium ($100 - $500)'),
            ('high', 'High (> $500)'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'low':
            return queryset.filter(price__lt=100)
        elif value == 'medium':
            return queryset.filter(price__gte=100, price__lte=500)
        elif value == 'high':
            return queryset.filter(price__gt=500)
        return queryset


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active']
    list_filter = ['category', 'is_active', PriceRangeFilter]
    search_fields = ['name', 'description']
    inlines = [ProductInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'parent_category_display']

    def parent_category_display(self, obj):
        return obj.parent_category.name if obj.parent_category else '-'
    parent_category_display.short_description = 'Parent Category'
