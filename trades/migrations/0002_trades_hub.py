# Generated by Django 3.0.7 on 2021-02-23 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade_search', '0002_delete_item'),
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='hub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trade_search.Hub'),
        ),
    ]
