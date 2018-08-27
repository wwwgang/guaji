# Generated by Django 2.0.7 on 2018-07-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('hp', models.FloatField()),
                ('power', models.FloatField()),
            ],
        ),
    ]