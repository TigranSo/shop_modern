# Generated by Django 4.1.4 on 2023-05-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_type_mis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_mis',
            field=models.CharField(choices=[('KO', 'Костюмы/спортивные'), ('KL', 'Костюмы/классические'), ('KF', 'Кофты'), ('BL', 'Блузы'), ('FU', 'Футболки'), ('BR', 'Брюки'), ('YU', 'Юбки'), ('PL', 'Платья'), ('XU', 'Худи'), ('SV', 'Свитера'), ('ZH', 'Жакеты'), ('VE', 'Ветровки'), ('KU', 'Куртки'), ('PU', 'Пуховики')], default='KO', max_length=2, verbose_name='Вид товара'),
        ),
    ]