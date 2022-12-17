# Generated by Django 4.0.6 on 2022-11-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_civil1_attendance_civil2_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('name', models.TextField()),
                ('logo', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
