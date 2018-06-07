############################################################  
# Graphite - Originally from https://github.com/seiffert/graphite-docker  
# Based on Phusion Image - https://github.com/phusion/baseimage-docker  
# ENV SUITABILITY: DEVELOPMENT  
############################################################  
  
FROM phusion/baseimage:0.9.15  
MAINTAINER Paul Seiffert <paul.seiffert@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
libapache2-mod-python libapache2-mod-wsgi \  
python python-twisted python-django python-django-tagging python-cairo python-
pyparsing python-memcache python-tz \  
git  
  
RUN git clone https://github.com/graphite-project/whisper.git \  
&& cd whisper \  
&& python setup.py install \  
&& cd .. \  
&& rm -fr whisper  
  
RUN git clone https://github.com/graphite-project/graphite-web.git \  
&& cd graphite-web \  
&& python setup.py install \  
&& rm -fr graphite-web  
  
COPY graphite.wsgi /opt/graphite/conf/graphite.wsgi  
COPY local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
COPY initial_data.json /opt/graphite/webapp/graphite/initial_data.json  
COPY vhost.conf /etc/apache2/sites-enabled/graphite.conf  
  
RUN mkdir -p /etc/httpd/wsgi \  
&& rm /etc/apache2/sites-enabled/000-default.conf \  
&& /etc/init.d/apache2 stop  
  
EXPOSE 80  
  
COPY run.sh /run.sh  
CMD ["/run.sh"]  

