from django.contrib import admin
from django.utils.html import format_html
from .models import Advertisement
from datetime import datetime

# Register your models here.

# создаем класс для отображения модели в панели администрирования
class AdvertismentAdmin (admin.ModelAdmin):
    list_display = ['id','title','description', 'price', 'created_time', 'colored_date',  'auction']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('общее', {
            'fields': ('title', 'description')
        }),
        ('финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )

    @admin.display (description = 'Обновлено')
    def colored_date(self, object):
        today = datetime.today().date()        
        if object.update_time.date() == today:            
            return format_html(
            '<span style="color: limegreen;"> Сегодня в {} </span>',
            object.update_time.strftime('%I:%M%p'),
        )
        else:
            return object.update_time

    @admin.action(description='убрать возможность торга') 
    # request - запрос с сайта
    # queryset - набор объектов, к которым применится созданный метод
    def make_auction_as_false(self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга') 
    def make_auction_as_true(self,request,queryset):
        queryset.update(auction=True)  
       
# отображаем нашу модель в панели администрирования
admin.site.register (Advertisement, AdvertismentAdmin)