from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html

# Register your models here.

# создаем класс для отображения модели в панели администрирования
class AdvertismentAdmin (admin.ModelAdmin):
    list_display = ['id', 'title','description', 'price', 'created_time', 'update_time', 'auction','get_html_image']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('общее', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )

    @admin.display (description='Миниатюра')
    def get_html_image(self, object):
        if object.image:
            return format_html(f"<img src = '{object.image.url}' width=50> ")
        else:
            return format_html(f"<img src = 'img/fire.png'>")
    
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