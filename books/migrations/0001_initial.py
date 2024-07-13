# Generated by Django 5.0.6 on 2024-06-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=14)),
                ('cover_pic', models.ImageField(upload_to='book_pics')),
            ],
        ),
    ]