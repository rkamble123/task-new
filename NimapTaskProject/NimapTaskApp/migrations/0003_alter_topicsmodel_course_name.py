# Generated by Django 4.1.4 on 2022-12-13 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NimapTaskApp', '0002_alter_usercreatemodel_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicsmodel',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NimapTaskApp.coursemodel'),
        ),
    ]
