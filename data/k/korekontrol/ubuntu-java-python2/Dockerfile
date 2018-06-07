FROM ubuntu:15.04  
MAINTAINER Marek Obuchowicz <marek@korekontrol.eu>  
  
# Setup python and java and base system  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=en_US.UTF-8  
  
RUN apt-get -q -y update && \  
apt-get upgrade -q -y && \  
apt-get install -q -y openjdk-8-jre-headless \  
libev4 libev-dev libpq-dev libldap2-dev libsasl2-dev libssl-dev \  
python-dev python-pip \  
python-numpy python-jinja2 python-suds python-psycopg2 python-pymysql \  
python-snappy python-redis python-sh python-six python-dnspython \  
python-pysnmp4 python-yaml python-requests python-setproctitle \  
python-yapsy python-dogpile.cache \  
supervisor  
  
ADD requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt && rm requirements.txt  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  

