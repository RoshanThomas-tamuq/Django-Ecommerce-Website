# Generated by Django 2.2 on 2020-08-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200803_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='123', max_length=20),
            preserve_default=False,
        ),
    ]
