# Generated by Django 5.0.7 on 2024-08-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0013_artifactreflection_intro_artifactreflection_second'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifactreflection',
            name='article_content2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
