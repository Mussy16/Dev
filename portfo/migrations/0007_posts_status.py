# Generated by Django 5.0.7 on 2024-07-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0006_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
