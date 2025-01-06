# Generated by Django 4.2 on 2025-01-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=800)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('website', models.URLField(max_length=300)),
                ('product_image', models.ImageField(default='../default_post_w4egx3', upload_to='images/')),
                ('image_alt', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
