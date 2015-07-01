# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from ratings.models import Rater

import pandas as pd

def load_rater_data(apps, schema_editor):
    rater_df = pd.read_csv('ratings/fixtures/users.csv', names=["rater_id", "gender", "age", "job", "zipcode"])
    for row in rater_df.iterrows():
        rater_obj = row[1]
        Rater.objects.create(
            rater=rater_obj.rater_id,
            gender=rater_obj.gender,
            age=rater_obj.age,
            job=rater_obj.job,
            zipcode=rater_obj.zipcode
        )



class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0009_auto_20150701_1524'),
    ]

    operations = [
        migrations.RunPython(load_rater_data)
    ]
