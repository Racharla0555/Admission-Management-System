# Generated by Django 4.1.3 on 2022-11-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_students_alter_apply_student_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='username',
            field=models.CharField(max_length=40),
        ),
    ]
