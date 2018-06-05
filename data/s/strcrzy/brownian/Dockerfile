FROM debian:jessie  
# FROM ubuntu:latest  
MAINTAINER stcrzy, https://github.com/strcrzy  
  
#Prevent daemon start during install  
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && \  
chmod +x /usr/sbin/policy-rc.d  
  
# Install Brownian Required Dependencies  
RUN apt-get -qq update && apt-get install -yq libcurl3-dev \  
uwsgi uwsgi-plugin-python python-pip git-core  
  
ENV DJANGO_SETTINGS_MODULE Brownian.settings  
  
# Install Brownian  
RUN \  
pip install git+https://github.com/grigorescu/Brownian.git && \  
sed -i "s/US\/Eastern/UTC/g" /usr/local/lib/python2.7/dist-
packages/Brownian/settings.py && \  
mkdir /opt/Brownian  
  
ADD /uwsgi/brownian.ini /opt/Brownian/  
  
CMD \  
sed -i "s/localhost:9200/`echo $ELASTICSEARCH_PORT_9200_TCP|cut -c 7-`/"
/usr/local/lib/python2.7/dist-packages/Brownian/settings.py && \  
python /usr/local/bin/django-admin.py syncdb --noinput && \  
chown -R nobody /opt/Brownian && \  
uwsgi --ini /opt/Brownian/brownian.ini  
  
EXPOSE 8080  

