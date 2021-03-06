# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLookup',
            fields=[
                ('user', models.OneToOneField(related_name='lookup', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
                ('scheme', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=255)),
            ],
        ),
    ]
