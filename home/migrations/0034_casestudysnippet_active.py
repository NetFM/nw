# Generated by Django 2.1.4 on 2018-12-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20181229_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudysnippet',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
