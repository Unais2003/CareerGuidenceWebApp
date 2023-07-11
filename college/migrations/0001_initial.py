# Generated by Django 3.2.16 on 2022-11-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('c_id', models.AutoField(db_column='c-id', primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=100)),
                ('college_location', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('e_mail', models.CharField(db_column='e-mail', max_length=100)),
                ('website', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'college',
                'managed': False,
            },
        ),
    ]