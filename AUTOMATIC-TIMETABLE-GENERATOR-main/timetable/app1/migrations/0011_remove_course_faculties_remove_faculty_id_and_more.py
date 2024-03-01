# Generated by Django 5.0.1 on 2024-02-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_course_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='faculties',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.AddField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(to='app1.course'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='fid',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]