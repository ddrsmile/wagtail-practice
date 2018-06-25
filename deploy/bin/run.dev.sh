#!/bin/bash

DEPLOYDIR=$( dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )")
ROOT=$( dirname $DEPLOYDIR)
NAME=${ROOT##*/}
DJANGODIR=${ROOT}/src
SOCKFILE=${DEPLOYDIR}/run/${NAME}.sock
USER=`id -un`
GROUP=`id -gn`
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=project.settings.dev
DJANGO_WSGI_MODULE=project.wsgi


cd $DEPLOYDIR
source ${DEPLOYDIR}/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ${DEPLOYDIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER  --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --log-level=debug \
    --log-file=-
