# Generated by Django 4.0.5 on 2022-07-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0002_alter_prediction_bundleref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='bundleRef',
            field=models.CharField(blank=True, choices=[('Bundle Four', 'Bundle Four'), ('Bundle Three', 'Bundle Three'), ('Bundle Two', 'Bundle Two'), ('Bundle One', 'Bundle One')], max_length=20, null=True),
        ),
    ]