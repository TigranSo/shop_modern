# Generated by Django 4.1.7 on 2023-05-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
            ],
            options={
                'verbose_name_plural': 'Заказ Звонков',
            },
        ),
    ]
