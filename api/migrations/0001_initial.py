# Generated by Django 2.2.3 on 2019-07-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='event', max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('total_minutes', models.IntegerField(default=0)),
                ('category', models.TextField(default='undefined', max_length=100)),
            ],
        ),
    ]
