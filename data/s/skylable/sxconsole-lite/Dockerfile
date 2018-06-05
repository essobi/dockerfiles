FROM centos:centos7  
MAINTAINER Skylable Dev-Team <dev-team@skylable.com>  
  
# Install deps  
RUN yum clean all && \  
yum -y update && \  
yum -y install epel-release && \  
yum clean all;  
  
RUN yum -y install nginx supervisor python-pip nodejs npm pwgen python-devel
py-bcrypt git gettext  
  
# prepare logs and workdirs  
WORKDIR /srv  
RUN mkdir -p media static sxconsole-lite  
VOLUME ["/srv/static/"]  
  
# install deps  
RUN pip install flup gunicorn  
WORKDIR /srv/sxconsole-lite  
COPY sxconsole-lite/requirements.txt sxconsole-lite/package.json sxconsole-
lite/i18n-manager.js /srv/sxconsole-lite/  
# install pip deps from requirements.txt and npm deps from packages.json  
RUN pip install -r requirements.txt  
  
# install npm and webpack  
RUN npm install npm -g  
# install javascript deps  
RUN npm install  
  
# build assets dir  
COPY sxconsole-lite/assets /srv/sxconsole-lite/assets  
RUN npm install webpack -g  
  
# process js translations  
RUN ./i18n-manager.js process  
  
# copy sxconsole app  
COPY sxconsole-lite/ /srv/sxconsole-lite  
COPY generate_conf.py /srv/generate_conf.py  
  
# config files  
COPY nginx-sxconsole-lite.conf /etc/nginx/conf.d/  
COPY nginx.conf /etc/nginx/  
COPY custom_50x.html /var/www/error_pages/  
COPY supervisord.conf /etc/supervisor/  
COPY run.sh /  
  
EXPOSE 443 8888  
CMD ["/run.sh"]  
  

