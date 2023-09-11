# Generated by Django 4.2.3 on 2023-09-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_item_discount_price_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('TV', 'Television'), ('AU', 'Audio'), ('AC', 'Air conditioner'), ('CM', 'Cameras'), ('AU', 'Refrigerators'), ('GC', 'Gas cookers'), ('FZ', 'Freezers'), ('WM', 'Washing machine'), ('FN', 'Fans'), ('KA', 'Kitchen Appliances')], max_length=2),
        ),
    ]