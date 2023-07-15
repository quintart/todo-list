# Generated by Django 4.2.1 on 2023-07-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('regno', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]