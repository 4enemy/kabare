from django.contrib import admin
from promotions.models import Promo

class PromoAdmin(admin.ModelAdmin):
    list_filter = ['posting_date']
    search_fields = ['header']
    date_hierarchy = 'posting_date' 
    fields = ['header', 'text']

admin.site.register(Promo, PromoAdmin)
