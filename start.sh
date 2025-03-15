#!/bin/bash
# source /home/olykhorovych/D/courses/project_copy/project/pressure/.venv/bin/activate && \
# python manage.py runserver 127.0.0.1:8083 --skip-checks
# export DATABASE_URL=postgresql://postgres:kCLwojVzmaItVMmtUziDPAyzVpCKBbGP@postgres.railway.internal:5432/railway
# export DEBUG=0

# python manage.py runscript start && \
#
echo "Starting start.sh script"

python manage.py migrate --settings=pressure.settings_dev && \
python manage.py populate_base --settings=pressure.settings_dev
echo "Starting webserver on 0.0.0.0:8000"
python manage.py runserver  0.0.0.0:8000 --settings=pressure.settings_dev

exit 0
