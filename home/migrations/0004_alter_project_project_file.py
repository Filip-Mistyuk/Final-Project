# Generated by Django 4.2.6 on 2023-10-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_project_title_project_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.FileField(default='test.py', upload_to='files/'),
        ),
    ]
