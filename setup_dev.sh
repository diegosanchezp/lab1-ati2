#!/bin/bash

python -m venv .venv
source .venv/bin/activate && pip install --cache-dir ./.cache -r requirements/local.txt && python manage.py migrate && python manage.py createsuperuser
