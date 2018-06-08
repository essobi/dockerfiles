# Use an official Python runtime as a parent image  
FROM python:2.7-slim  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
#RUN apt-get update -y \  
# && apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-
dev  
  
# Install any needed packages specified in requirements.txt use --no-cache-dir
if you don't want to cache  
RUN pip install --no-cache-dir -r requirements.txt  
#RUN pip3 install --no-cache-dir -r requirements.txt  
  
RUN apt-get -qq update  
RUN apt-get install -y python-dev python-setuptools supervisor git-core
libmysqlclient-dev postgresql-server-dev-all libpq-dev  
  
#RUN apk update && \  
# apk add --virtual build-deps gcc python-dev musl-dev && \  
# apk add postgresql-dev  
  
#RUN apt install libmysqlclient-dev  
  
#RUN psycopg2 LIBRARY_PATH=/usr/local/lib/python2.7/dist-packages  
#RUN pycurl LIBRARY_PATH=/usr/local/lib/python2.7/dist-packages  
#RUN pip install -H pycurl  
  
RUN easy_install pip  
RUN pip install ez_setup  
#RUN pip install mysqlclient  
#RUN pip install pystan  
RUN pip install virtualenv  
#RUN pip install psutil  
#RUN pip install uwsgi  
RUN virtualenv --no-site-packages /opt/ve/djdocker  
#ADD . /opt/apps/djdocker  
#ADD .docker/supervisor.conf /opt/supervisor.conf  
#ADD .docker/run.sh /usr/local/bin/run  
  
#Run set -ex\  
# && apk add --no-cache --virtual .build-deps \  
# gcc \  
# make \  
# libc-dev \  
# musl-dev \  
# linux-headers \  
# pcre-dev \  
# postgresql-dev \  
# && pyvenv /venv \  
# && /venv/bin/pip install -U pip \  
# && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip instsall --no-cache-
dir -r /requirements.txt" \  
# && runDeps="$( \  
# scanelf --needed --nobanner --recursive /venv \  
# | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
# | sort -u \  
# | xargs -r apk info -- installed \  
# | sort -u \  
# )"\  
# && apk add --virtual .python-rundeps $runDeps \  
# && apk del .build-deps  
  
# Make port 80 available to the world outside this container  
EXPOSE 80  
  
# Define environment variable  
ENV NAME World  
  
#Run DATABASE_URL=none /venv/bin/python manage.py collectstatic --noinput  
  
# Run app.py when the container launches  
CMD ["python", "app.py"]

