# Generated by Django 5.0.1 on 2024-01-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_dept_student_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]