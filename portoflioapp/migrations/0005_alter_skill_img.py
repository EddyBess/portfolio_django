# Generated by Django 4.1.1 on 2022-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portoflioapp", "0004_skill_project_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="img",
            field=models.ImageField(upload_to="images/"),
        ),
    ]