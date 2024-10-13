# Generated by Django 5.0.7 on 2024-08-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0010_remove_artifactreflection_article_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifactreflection',
            name='additional_image',
            field=models.ImageField(blank=True, null=True, upload_to='artifacts/'),
        ),
        migrations.AddField(
            model_name='artifactreflection',
            name='article_content',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
