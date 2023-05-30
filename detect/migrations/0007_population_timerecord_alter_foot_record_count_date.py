# Generated by Django 4.0 on 2023-05-22 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0006_population_population_record_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population_TimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_1', models.IntegerField(default=0, null=True)),
                ('time_2', models.IntegerField(default=0, null=True)),
                ('time_3', models.IntegerField(default=0, null=True)),
                ('time_4', models.IntegerField(default=0, null=True)),
                ('time_5', models.IntegerField(default=0, null=True)),
                ('time_6', models.IntegerField(default=0, null=True)),
                ('time_7', models.IntegerField(default=0, null=True)),
                ('time_8', models.IntegerField(default=0, null=True)),
                ('time_9', models.IntegerField(default=0, null=True)),
                ('time_10', models.IntegerField(default=0, null=True)),
                ('time_11', models.IntegerField(default=0, null=True)),
                ('time_12', models.IntegerField(default=0, null=True)),
                ('time_13', models.IntegerField(default=0, null=True)),
                ('time_14', models.IntegerField(default=0, null=True)),
                ('time_15', models.IntegerField(default=0, null=True)),
                ('time_16', models.IntegerField(default=0, null=True)),
                ('time_17', models.IntegerField(default=0, null=True)),
                ('time_18', models.IntegerField(default=0, null=True)),
                ('time_19', models.IntegerField(default=0, null=True)),
                ('time_20', models.IntegerField(default=0, null=True)),
                ('time_21', models.IntegerField(default=0, null=True)),
                ('time_22', models.IntegerField(default=0, null=True)),
                ('time_23', models.IntegerField(default=0, null=True)),
                ('time_24', models.IntegerField(default=0, null=True)),
                ('count_date', models.DateTimeField(default=datetime.datetime(2023, 5, 22, 0, 38, 53, 931328))),
            ],
        ),
        migrations.AlterField(
            model_name='foot_record',
            name='count_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 22, 0, 38, 53, 931328)),
        ),
    ]