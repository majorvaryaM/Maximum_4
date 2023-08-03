from django.db import models

# Create your models here.
# создаем класс с описанием структуры будущей таблицы (наследуемся от класса Model)
class Advertisement(models.Model):
    # создаем заголовок объявления 
    # CharField - класс, обозначающий символьное поле (набор символов), подходит для небольших текстов
    title = models.CharField('Заголовок',max_length=128)
    # создаем описание объявления
    # TextField - класс, обозначающий строковое поле больших размеров
    description = models.TextField ('Описание')
    # создаем цену 
    # Decimal - дробное число с фиксированной точностью (похоже на float в Python)
    # max_digits - максимальное кол-во цифр в числе
    # decival_places - кол-во знаков после запятой
    price = models.DecimalField('Цена', max_digits=10,decimal_places=2)
    # создаем возможность торговаться
    # BooleanField - логический тип данных (истина или ложь)
    auction = models.BooleanField('Торг',help_text='Отметьте, уместен ли торг')
    # создаем дату размещения объявления 
    # auto_now_add=True - сразу получаем дату в момент созданию объявления
    created_time = models.DateTimeField(auto_now_add=True)
    # создаем дату обновления объявления
    # auto_now=True - получаем дату в момент обновления объявления
    update_time = models.DateTimeField(auto_now=True)
    # называем таблицу
    class Meta:
        db_table = 'advertisements'
    # создаем функцию для вызова значений
    def __str__(self):
	    return f"id={self.id}, title={self.title}, price={self.price}"