FROM ubuntu:xenial  
  
MAINTAINER Simon Biggs <mail@simonbiggs.net>  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
git \  
libapache2-mod-wsgi \  
libpq-dev \  
postgresql \  
python-pip \  
python-psycopg2  
  
EXPOSE 80  
EXPOSE 8000  
RUN mkdir --parents /var/www/qatrackplus/db  
WORKDIR /var/www/qatrackplus/  
  
COPY requirements /var/www/qatrackplus/requirements  
RUN pip install -r requirements/base.txt  
  
COPY qatrack /var/www/qatrackplus/qatrack  
  
COPY deploy /var/www/qatrackplus/deploy  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
RUN cp /var/www/qatrackplus/deploy/docker_apache24.conf /etc/apache2/sites-
available/qatrack.conf  
RUN ln -s /etc/apache2/sites-available/qatrack.conf /etc/apache2/sites-
enabled/qatrack.conf  
  
USER postgres  
  
RUN service postgresql start && \  
psql -c "ALTER USER postgres with encrypted password 'postgresspass';" && \  
psql -c "CREATE DATABASE qatrackdb;" && \  
psql -c "CREATE USER qatrack with PASSWORD 'qatrackpass';" && \  
psql -c "GRANT ALL PRIVILEGES ON DATABASE qatrackdb to qatrack;"  
  
USER root  
  
RUN cp deploy/docker_postgres.py qatrack/local_settings.py  
RUN cp deploy/docker_pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf  
  
COPY manage.py /var/www/qatrackplus/manage.py  
COPY fixtures /var/www/qatrackplus/fixtures  
RUN service postgresql start && \  
python manage.py syncdb --noinput && \  
echo "from django.contrib.auth.models import User;
User.objects.create_superuser('admin', 'myemail@example.com', 'admin')" |
python manage.py shell && \  
python manage.py migrate && \  
python manage.py loaddata fixtures/defaults/*/* && \  
python manage.py collectstatic --noinput  
  
COPY . /var/www/qatrackplus/  
  
RUN chmod 777 -R /var/www/qatrackplus  
  
CMD service postgresql start && service apache2 start && tail -f /dev/null  
  

