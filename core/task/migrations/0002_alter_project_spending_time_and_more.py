# Generated by Django 4.2.23 on 2025-07-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="spending_time",
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name="subproject",
            name="spending_time",
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name="task",
            name="spending_time",
            field=models.DurationField(),
        ),
    ]
