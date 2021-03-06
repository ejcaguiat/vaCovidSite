# Generated by Django 3.0.8 on 2020-08-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200818_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='deathIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='case',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='case',
            name='negativeIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='case',
            name='positiveIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='case',
            name='recovered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='case',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='case',
            name='positive',
            field=models.IntegerField(default=0),
        ),
    ]
