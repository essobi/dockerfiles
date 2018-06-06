FROM ubuntu:14.04  
MAINTAINER CREATIVE AREA <contact@creative-area.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GRAPHITEWEB_USERNAME root  
ENV GRAPHITEWEB_PASSWORD root  
ENV GRAPHITEWEB_EMAIL root@localhost  
  
RUN apt-get -qq update && apt-get install -y \  
python-dev \  
python-pip \  
python-cairo \  
python-tz \  
python-ldap \  
python-txamqp \  
python-pyparsing \  
python-django \  
python-django-tagging \  
python-memcache \  
python-rrdtool \  
expect \  
git \  
gunicorn \  
nginx-light \  
supervisor  
  
RUN git clone https://github.com/graphite-project/graphite-web.git
/usr/local/src/graphite-web  
RUN git clone https://github.com/graphite-project/carbon.git
/usr/local/src/carbon  
RUN git clone https://github.com/graphite-project/whisper.git
/usr/local/src/whisper  
#RUN git clone https://github.com/graphite-project/ceres.git
/usr/local/src/ceres  
RUN cd /usr/local/src/whisper && python setup.py install  
#RUN cd /usr/local/src/ceres && python setup.py install  
RUN cd /usr/local/src/carbon && python setup.py install  
RUN cd /usr/local/src/graphite-web && python setup.py install  
  
COPY conf/local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
COPY conf/django_admin_init.sh /usr/local/bin/django_admin_init.sh  
COPY conf/carbon.conf /opt/graphite/conf/carbon.conf  
COPY conf/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf  
COPY conf/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf  
  
RUN /usr/local/bin/django_admin_init.sh  
  
RUN PYTHONPATH=/opt/graphite/webapp /usr/bin/django-admin collectstatic
--noinput --settings=graphite.settings  
  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
EXPOSE 2003  
EXPOSE 2004  
EXPOSE 7002  
VOLUME ["/opt/graphite/conf"]  
VOLUME ["/opt/graphite/storage/whisper"]  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

