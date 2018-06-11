FROM ubuntu:16.04  
COPY debathena-archive.asc /tmp/  
RUN apt-key add /tmp/debathena-archive.asc  
COPY debathena.list /etc/apt/sources.list.d/  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
comerr-dev \  
cython \  
debathena-hesiod-config \  
debathena-zephyr-config \  
debhelper \  
git \  
libzephyr-dev \  
postgresql-client \  
python \  
python-all-dev \  
python-dev \  
python-distribute \  
python-psycopg2 \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ZephyrPlus/requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt \  
raven  
  
COPY ZephyrPlus /ZephyrPlus/  
  
RUN chown -R www-data:www-data /ZephyrPlus \  
&& touch /var/log/tornado.log /var/log/zpd.log \  
&& chown www-data:www-data /var/log/tornado.log /var/log/zpd.log \  
&& mkdir /var/www && chown www-data:www-data /var/www \  
&& mkdir /var/db && chown www-data:www-data /var/db  
  
USER www-data  
WORKDIR /ZephyrPlus  
RUN ./manage.py migrate \  
&& mv zephyrs.db /var/db/ \  
&& ln -s /var/db/zephyrs.db zephyrs.db  
  
VOLUME /var/db /var/log  
  
CMD zhm && (./start_tornado.sh &) && /bin/bash  

