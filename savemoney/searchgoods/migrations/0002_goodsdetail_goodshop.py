# Generated by Django 2.1 on 2018-08-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchgoods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsdetail',
            name='goodshop',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
