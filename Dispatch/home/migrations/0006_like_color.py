# Generated by Django 3.1.7 on 2021-03-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='color',
            field=models.CharField(choices=[('#adadfd', '#adadfd'), ('#fa6342', '#fa6342')], default='#adadfd', max_length=8),
        ),
    ]
