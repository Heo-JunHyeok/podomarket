# Generated by Django 4.2.3 on 2023-07-21 04:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0003_alter_user_address_alter_user_kakao_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]