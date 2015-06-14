#!/bin/sh
set -e

outpostd &
OUTPOSTD_PID=$!

./manage.py runserver &
RUNSERVER_PID=$!

sleep 1

sigpolld &
SIGPOLLD_PID=$!

read foo

kill ${OUTPOSTD_PID} ${SIGPOLLD_PID} ${RUNSERVER_PID}
