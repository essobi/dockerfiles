FROM metabrainz/python:2.7  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
git \  
libpq-dev \  
libffi-dev \  
libssl-dev \  
node-less \  
node-clean-css \  
redis-tools \  
uwsgi \  
uwsgi-plugin-python \  
&& rm -rf /var/lib/apt/lists/*  
  
# PostgreSQL client  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
ENV PG_MAJOR 9.5  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends postgresql-client-$PG_MAJOR \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /code  
WORKDIR /code  
  
# MessyBrainz  
RUN git clone https://github.com/metabrainz/messybrainz-server.git messybrainz  
WORKDIR /code/messybrainz  
RUN pip install -r requirements.txt  
RUN python setup.py install  
  
# ListenBrainz  
WORKDIR /code  
RUN git clone https://github.com/metabrainz/listenbrainz-server.git
listenbrainz  
WORKDIR /code/listenbrainz  
RUN pip install -r requirements.txt  
  
# Node  
#RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
#RUN apt-get install -y nodejs  
#RUN npm install less-plugin-clean-css  
# Compile the CSS  
# TODO: Bring this back  
# RUN lessc --clean-css webserver/static/css/main.less >
webserver/static/css/main.css  
RUN lessc webserver/static/css/main.less > webserver/static/css/main.css  
  
# Consul Template service is already set up with the base image.  
# Just need to copy the configuration.  
COPY ./docker/prod/consul-template.conf /etc/consul-template.conf  
  
COPY ./docker/prod/uwsgi/uwsgi.service /etc/service/uwsgi/run  
RUN chmod 755 /etc/service/uwsgi/run  
COPY ./docker/prod/uwsgi/uwsgi.ini /etc/uwsgi/uwsgi.ini  
  
# setup a log dir  
RUN mkdir /logs  
RUN chown -R daemon:daemon /logs  

