# Generated by Django 4.0.5 on 2022-07-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0014_alter_prediction_bundleref_alter_prediction_dailyref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='bundleRef',
            field=models.CharField(blank=True, choices=[('Bundle Three', 'Bundle Three'), ('Bundle Two', 'Bundle Two'), ('Bundle One', 'Bundle One'), ('Bundle Four', 'Bundle Four')], max_length=20, null=True),
        ),
    ]
