# Generated by Django 4.0.2 on 2022-02-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(blank=True, max_length=50, null=True)),
                ('currentemp', models.FloatField(blank=True, null=True)),
                ('fellslike', models.FloatField(blank=True, null=True)),
                ('averagetemp', models.IntegerField(blank=True, null=True)),
                ('citylat', models.FloatField(blank=True, null=True)),
                ('citylon', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
