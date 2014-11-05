# -*- coding: utf-8 -*-
from __future__ import unicode_literals

chdir = "/home/ubuntu/workshop-deploying-django/coffeecake"
bind = "unix:/home/ubuntu/coffeecake.sock"
env = 'DJANGO_SETTINGS_MODULE="coffeecake.settings.production"'
workers = 2
