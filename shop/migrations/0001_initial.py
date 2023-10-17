# Generated by Django 4.1.7 on 2023-05-01 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Корзина', 'Корзина'), ('Ожидает платежа', 'Ожидает платежа'), ('Оплачено', 'Оплачено')], default='Корзина', max_length=32, verbose_name='Cтатус')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Cумма')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('pickup', models.CharField(blank=True, max_length=100, verbose_name='Cамовывоз')),
                ('time_samo', models.CharField(blank=True, max_length=50, verbose_name='Время самовывоза')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='Улица')),
                ('home', models.CharField(blank=True, max_length=50, verbose_name='Дом')),
                ('podezd', models.CharField(blank=True, max_length=50, verbose_name='Подъезд')),
                ('etaj', models.CharField(blank=True, max_length=50, verbose_name='Этаж')),
                ('kvartir', models.CharField(blank=True, max_length=30, verbose_name='Квартира/офис')),
                ('domofon', models.CharField(max_length=30, verbose_name='Удобный способ оплаты')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('file', models.FileField(blank=True, null=True, upload_to='file', verbose_name='Файл')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время заказа')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('type_mis', models.CharField(max_length=100, verbose_name='Вид товара')),
                ('code', models.CharField(max_length=255, verbose_name='Код товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='url изображения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Изображение')),
                ('note', models.TextField(blank=True, null=True, verbose_name='записка')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Cумма')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Платеж',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Скидка')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name_plural': 'Элемент заказа',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.payment', verbose_name='Платеж'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
