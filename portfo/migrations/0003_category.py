# Generated by Django 5.0.7 on 2024-07-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
