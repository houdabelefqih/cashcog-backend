#!/bin/sh
set -e

python manage.py migrate --no-input

exec "$@"