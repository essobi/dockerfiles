FROM ubuntu:16.04  
MAINTAINER Lionel  
  
ENV GRAPHITE_VERSION 0.9.15  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >>
/etc/apt/sources.list  
  
# Install required packages  
RUN apt-get -y update && \  
apt-get -y install \  
python-ldap \  
python-cairo \  
python-django \  
python-twisted \  
python-django-tagging \  
python-simplejson \  
python-memcache \  
python-pysqlite2 \  
python-pip \  
gunicorn \  
supervisor \  
nginx-light  
RUN pip install whisper==$GRAPHITE_VERSION  
RUN pip install carbon==$GRAPHITE_VERSION \--install-option="--
prefix=/var/lib/graphite" \--install-option="--install-
lib=/var/lib/graphite/lib"  
RUN pip install graphite-web==$GRAPHITE_VERSION \--install-option="--
prefix=/var/lib/graphite" \--install-option="--install-
lib=/var/lib/graphite/webapp"  
  
# Add supervisord and nginx config  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add graphite config  
ADD ./local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py  
ADD ./carbon.conf /var/lib/graphite/conf/carbon.conf  
ADD ./storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf  
  
# Initializing whisper and graphite-web  
RUN mkdir -p /var/lib/graphite/storage/whisper  
RUN touch /var/lib/graphite/storage/graphite.db
/var/lib/graphite/storage/index  
RUN chown -R www-data /var/lib/graphite/storage  
RUN chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper  
RUN chmod 0664 /var/lib/graphite/storage/graphite.db  
RUN cd /var/lib/graphite/webapp/graphite && python manage.py syncdb --noinput  
RUN cp /var/lib/graphite/conf/graphite.wsgi.example
/var/lib/graphite/webapp/graphite/graphite_wsgi.py  
  
VOLUME /var/lib/graphite/conf  
VOLUME /var/lib/graphite/storage/log  
VOLUME /var/lib/graphite/storage/whisper  
  
# Nginx  
EXPOSE :8080  
# Carbon line receiver port  
EXPOSE :2003  
# Carbon pickle receiver port  
EXPOSE :2004  
# Carbon cache query port  
EXPOSE :7002  
cmd ["/usr/bin/supervisord"]  

