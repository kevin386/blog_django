# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150308_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='excerpt',
            new_name='reference',
        ),
    ]
