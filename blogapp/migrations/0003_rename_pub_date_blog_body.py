# Generated by Django 3.2.2 on 2021-05-11 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_departdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='body',
        ),
    ]
