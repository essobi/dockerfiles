FROM debian:stable  
MAINTAINER Olivier Sallou <olivier.sallou@irisa.fr>  
  
LABEL status="for development or to get latest features"  
LABEL description="Batch scheduling system in containers. This image contains
\  
all godocker components: web, scheduler and watchers. \  
Config should be overriden in /opt/godocker/go-d.ini \  
file. Default configuration does not provide mail and only fake \  
authentication."  
  
EXPOSE 6543  
WORKDIR /opt/go-docker  
  
ENV admin="root"  
ENV swarm_url="tcp://god-swarm:2375"  
# ENV PYTHONPATH="/usr/lib/python2.7/site-packages:${PYTHONPATH}"  
#ENV PYRAMID_ENV="prod"  
ENV PYRAMID_ENV="dev"  
ENV prometheus_multiproc_dir="/tmp/godocker-multiproc"  
RUN mkdir -p /tmp/godocker-multiproc  
RUN apt-get update  
RUN apt-get install -y git python3-dev libldap2-dev gcc libsasl2-dev \  
python3-setuptools apt-transport-https wget \  
openssl libpython3-dev libffi-dev libssl-dev protobuf-compiler python3-pip \  
openjdk-8-jre-headless libcurl3 libsvn1  
  
RUN cd /opt && git clone -b develop https://bitbucket.org/osallou/go-
docker.git  
RUN cd /opt && git clone -b develop https://bitbucket.org/osallou/go-docker-
web.git  
# RUN easy_install pip  
RUN pip3 install -U setuptools  
RUN cd /opt/go-docker && pip3 install -r requirements.txt  
RUN cd /opt/go-docker && python3 setup.py develop  
RUN cd /opt/go-docker-web && pip3 install -r requirements.txt  
RUN cd /opt/go-docker-web && python3 setup.py develop  
RUN pip3 install godocker_cli  
RUN cd /opt/go-docker-web && cp production.ini.example production.ini  
RUN cd /opt/go-docker-web && sed -i 's;global_properties =.*;global_properties
= /opt/go-docker/go-d.ini;g' production.ini  
RUN cd /opt/go-docker-web && sed -i 's;admin =.*;admin = '${admin}';g'
production.ini  
RUN cd /opt/go-docker && cp go-d.ini.sample go-d.ini  
RUN cd /opt/go-docker && sed -i "s;plugins_dir:.*;plugins_dir: '/opt/go-
docker/plugins';g" go-d.ini  
RUN cd /opt/go-docker && sed -i "s;shared_dir:.*;shared_dir:
'/opt/godshared';g" go-d.ini  
RUN cd /opt/go-docker && sed -i "s;mongo_url:.*;mongo_url: 'mongodb://god-
mongo:27017';g" go-d.ini  
RUN cd /opt/go-docker && sed -i "s;redis_host:.*;redis_host: 'god-redis';g"
go-d.ini  
RUN cd /opt/go-docker && sed -i "s;influxdb_host:.*;influxdb_host: null;g"
go-d.ini  
RUN cd /opt/go-docker && sed -i "s;prometheus_exporter:.*;prometheus_exporter:
'god-web:6543';g" go-d.ini  
RUN cd /opt/go-docker && sed -i "s;docker_url:.*;docker_url:
'"${swarm_url}"';g" go-d.ini  
  
RUN apt-get install -y curl gnupg2  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN cd /opt/go-docker-web/godweb/webapp && npm install && npm install -g bower
&& bower install --allow-root  
  
RUN mkdir -p /var/log/go-docker  

