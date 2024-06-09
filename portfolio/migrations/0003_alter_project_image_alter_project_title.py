# Generated by Django 4.2.6 on 2024-02-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="portfolio/images/"),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
