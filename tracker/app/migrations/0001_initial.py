# Generated by Django 3.2.6 on 2021-08-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode_id', models.CharField(max_length=20)),
                ('activation', models.BooleanField()),
                ('activation_name', models.TextField()),
                ('sender_firstname', models.TextField()),
                ('sender_add', models.TextField()),
                ('sender_subdis', models.TextField()),
                ('sender_dis', models.TextField()),
                ('sender_code', models.TextField()),
                ('recip_firstname', models.TextField()),
                ('recip_lastname', models.TextField()),
                ('recip_add', models.TextField()),
                ('recip_subdis', models.TextField()),
                ('recip_dis', models.TextField()),
                ('recip_code', models.TextField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('depth', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
    ]