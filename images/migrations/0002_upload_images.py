# Generated by Django 4.1 on 2022-12-13 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
