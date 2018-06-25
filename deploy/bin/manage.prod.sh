#!/bin/bash

DEPLOYDIR=$( dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )")
ROOT=$( dirname $DEPLOYDIR)
NAME=${ROOT##*/}
DJANGODIR=${ROOT}/src
DJANGO_SETTINGS_MODULE=project.settings.prod
source ${DEPLOYDIR}/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

exec ${DJANGODIR}/manage.py "$@"
