# Generated by Django 2.1.1 on 2018-09-08 07:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='normaluserform',
            new_name='normal_user_form',
        ),
        migrations.AlterModelOptions(
            name='normal_user_form',
            options={'verbose_name_plural': 'normal_user_form'},
        ),
    ]
