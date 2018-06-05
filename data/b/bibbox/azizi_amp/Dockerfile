  
FROM python:2.7  
# maintainer of the repo  
LABEL authors = "Wangoru Kihara <wangoru.kihara@badili.co.ke>, Azizi
Biorepository <azizibiorepository@cgiar.org>, Steve Kemp <s.kemp@cgiar.org>"  
  
WORKDIR /opt  
  
# install git  
RUN apt-get update \  
&& apt-get -y install apt-utils wget qt5-default qtbase5-private-dev
qtdeclarative5-dev cmake \  
&& sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main"
> /etc/apt/sources.list.d/pgdg.list' \  
# && sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release
-cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update \  
&& apt-get -y install postgresql-9.4-postgis-2.1 binutils libproj-dev gdal-bin
memcached libmemcached-dev python-pip \  
python-dev git libssl-dev libpq-dev gfortran libatlas-base-dev libjpeg-dev
libxml2-dev libxslt1-dev zlib1g-dev \  
python-software-properties ghostscript openjdk-7-jre libffi-dev libssl-dev
rabbitmq-server uwsgi \  
&& git clone https://github.com/onaio/onadata.git  
  
WORKDIR /opt/onadata  
  
RUN git checkout 394f06e483c88cdfc7aab31673310e99742c5c3e \  
&& git checkout -b classic_ona \  
&& cp onadata/settings/default_settings.py onadata/settings/local_settings.py
\  
&& sed -i 's/127\\.0\\.0\\.1/azizi_amp_db/' onadata/settings/local_settings.py
\  
&& sed -i "s/'PASSWORD': ''/'PASSWORD': 'onadata'/"
onadata/settings/local_settings.py \  
&& python2 -m pip install -r requirements/makefile_dependencies.pip \  
&& python2 -m pip install django-digest django-utils\  
&& pip install -r requirements/base.pip  
  
WORKDIR /opt/onadata/docs  
RUN make html  
WORKDIR /opt/onadata  
  
RUN apt-get -y install rabbitmq-server \  
&& wget
https://gist.githubusercontent.com/soloincc/6bfe3791f73afdccad8a1ddf07404729/raw/d0f78668cb83c2c957c015e89aaa1231dca44e29/celeryd-
ona \  
&& sed -i "s/onadata\\-venv/onadata/" celeryd-ona \  
&& sed -i "s/celery\\-venv/celery/" celeryd-ona \  
&& mv celeryd-ona /etc/default/celeryd-ona \  
&& cp /etc/default/celeryd-ona /etc/init.d/ \  
&& chmod +x /etc/init.d/celeryd-ona \  
&& update-rc.d celeryd-ona defaults \  
&& service celeryd-ona start  
  
RUN apt-get -y install nginx \  
&& wget
https://gist.githubusercontent.com/soloincc/ce791bc0f4bd4b1c8b59f6c321711f6e/raw/32febd14088284dd5bc3a94ebedfd572fad56070/nginx-
onadata \  
# Edit the config file appropriately \  
&& sed -i "s/onadata\\-venv/onadata/" nginx-onadata \  
&& sed -i "s/ona\\-venv/ona/" nginx-onadata \  
&& mv nginx-onadata /etc/nginx/sites-available/onadata \  
&& ln -s /etc/nginx/sites-available/onadata /etc/nginx/sites-enabled/onadata \  
&& unlink /etc/nginx/sites-enabled/default \  
&& service nginx restart  
  
WORKDIR /opt  
  
# install odktoolkit  
RUN git clone https://github.com/ilri/odktools.git  
  
WORKDIR /opt/odktools  
RUN git submodule update --init --recursive  
  
WORKDIR /opt/odktools/3rdparty/qjson  
RUN mkdir build  
WORKDIR /opt/odktools/3rdparty/qjson/build  
  
RUN cmake /opt/odktools/3rdparty/qjson \  
&& make \  
&& make install  
  
WORKDIR /opt/odktools  
  
RUN qmake \  
&& make  
  
ADD scripts /opt/scripts  
WORKDIR /opt/scripts  
RUN chmod a+x *.sh  
  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]  
  

