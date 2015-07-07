# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from ratings.models import Rater
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    counter = 0
    timer = 0
    raters = Rater.objects.all()
    for obj in raters:
        obj.user = User.objects.create(username=str(obj.rater))
        obj.user.set_password("password")
        obj.user.save()
        obj.save()
        timer += 1
        counter += 1
        if counter > 100:
            counter -= 90
        marks = '*' * counter
        percentage = round(((timer / len(raters)) * 100), 2)
        print('{}{}'.format(percentage, marks))



class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0015_rater_user'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]
