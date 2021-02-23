# Generated by Django 3.0.7 on 2021-02-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Item', '0004_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='trades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item1', to='Item.Item')),
                ('item2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item2', to='Item.Item')),
            ],
        ),
    ]
