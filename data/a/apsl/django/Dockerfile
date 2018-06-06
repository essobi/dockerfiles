FROM apsl/circusbase  
MAINTAINER Bernardo Cabezas <bcabezas@apsl.net>  
  
#nginx  
RUN \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install nginx-full && \  
apt-get clean  
  
ADD circus.d/nginx.ini.tpl /etc/circus.d/  
ADD setup.d/nginx /etc/setup.d/30-nginx  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
#RUN chown www-data /logs  
VOLUME /logs  
  
# Things required for a python/pip environment  
RUN \  
apt-get update && \  
apt-get -y -q install git mercurial curl build-essential && \  
apt-get -y -q install python python-dev python-distribute python-pip && \  
apt-get -y -q install inetutils-ping dnsutils && \  
apt-get -y -q install libpq-dev libmysqlclient-dev libxml2-dev libxslt1-dev
libssl-dev && \  
apt-get clean  
  
# nodejs  
RUN \  
apt-get install nodejs npm && apt-get clean && \  
npm install -g less && \  
ln -s /usr/bin/nodejs /usr/bin/node  
  
# django user and dirs  
RUN \  
addgroup --system --gid 500 django;\  
adduser --system --shell /bin/bash --gecos 'Django app user' \--uid 500 --gid
500 --disabled-password --home /code django ;\  
mkdir -p /data/media; mkdir -p /data/static ;\  
chown django.django /data -R  
# django conf  
ADD setup.d/django /etc/setup.d/40-django  
ADD circus.d/celery_worker.ini.tpl /etc/circus.d/  
ADD circus.d/celery_beat.ini.tpl /etc/circus.d/  
ADD circus.d/flower.ini.tpl /etc/circus.d/  
ADD conf/bashrc /code/.bashrc  
RUN chown django.django /code -R  
ADD conf/manage /usr/local/bin/  
  
# django celery  
# virtualenv  
RUN \  
pip --no-input install virtualenv==1.11.6 && \  
pip --no-input install pew==0.1.14 && \  
pip --no-input install chaussette==1.2 && \  
pip --no-input install PyYAML==3.11 # needed for install_crons  
  
# create Virtualenv  
ENV HOME /code  
ENV SHELL bash  
ENV WORKON_HOME /code  
WORKDIR /code/src  
RUN su -c "pew-new env -i ipython" django  
  
ADD circus.d/django.ini.tpl /etc/circus.d/  
  
# nginx django flower circusd  
EXPOSE 8000 80 8084 8888  

