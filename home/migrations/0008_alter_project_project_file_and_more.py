# Generated by Django 4.2.6 on 2023-10-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_project_project_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.FileField(default='there is no file.py', upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_file2',
            field=models.FileField(default='there is no file.py', upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_file3',
            field=models.FileField(default='there is no file.py', upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_file4',
            field=models.FileField(default='there is no file.py', upload_to='files/'),
        ),
    ]
