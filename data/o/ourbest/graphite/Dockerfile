FROM ubuntu:16.04  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
#RUN echo deb http://archive.ubuntu.com/ubuntu $(lsb_release -cs) main
universe > /etc/apt/sources.list.d/universe.list  
RUN apt-get -y update\  
&& apt-get -y upgrade  
  
# dependencies  
RUN apt-get -y --force-yes install vim\  
nginx\  
python-dev\  
python-flup\  
python-pip\  
python-ldap\  
expect\  
git\  
memcached\  
sqlite3\  
libcairo2\  
libcairo2-dev\  
python-cairo\  
python-rrdtool\  
pkg-config\  
nodejs  
  
# python dependencies  
# install graphite  
RUN git clone \--depth 1 https://github.com/graphite-project/graphite-web.git
/usr/local/src/graphite-web  
WORKDIR /usr/local/src/graphite-web  
  
RUN apt-get -y install libffi-dev  
RUN pip install -r requirements.txt  
  
RUN python ./setup.py install  
ADD conf/opt/graphite/conf/*.conf /opt/graphite/conf/  
ADD conf/opt/graphite/webapp/graphite/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py  
#ADD conf/opt/graphite/webapp/graphite/app_settings.py
/opt/graphite/webapp/graphite/app_settings.py  
RUN cp /usr/local/src/graphite-web/webapp/manage.py /opt/graphite/webapp/  
  
WORKDIR /opt/graphite/webapp  
RUN mkdir /var/log/graphite  
  
RUN python manage.py collectstatic --noinput  
  
# install whisper  
RUN git clone \--depth 1 https://github.com/graphite-project/whisper.git
/usr/local/src/whisper  
WORKDIR /usr/local/src/whisper  
RUN python ./setup.py install  
  
# install carbon  
RUN git clone \--depth 1 https://github.com/graphite-project/carbon.git
/usr/local/src/carbon  
WORKDIR /usr/local/src/carbon  
RUN python ./setup.py install  
  
# install statsd  
RUN git clone https://github.com/etsy/statsd.git /opt/statsd  
ADD conf/opt/statsd/config.js /opt/statsd/config.js  
  
# config nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD conf/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD conf/etc/nginx/sites-enabled/graphite-statsd.conf /etc/nginx/sites-
enabled/graphite-statsd.conf  
  
# init django admin  
#ADD conf/usr/local/bin/django_admin_init.exp
/usr/local/bin/django_admin_init.exp  
#RUN /usr/local/bin/django_admin_init.exp  
# logging support  
RUN mkdir -p /var/log/carbon /var/log/graphite /var/log/nginx  
ADD conf/etc/logrotate.d/graphite-statsd /etc/logrotate.d/graphite-statsd  
  
# daemons  
ADD conf/etc/supervisord.conf /etc/  
  
# default conf setup  
ADD conf /etc/graphite-statsd/conf  
  
# cleanup  
RUN apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install cachetools supervisor gevent django==1.8.15  
WORKDIR /opt/graphite/webapp  
  
RUN python manage.py migrate  
  
# defaults  
EXPOSE 80 2003-2004 2023-2024 8125/udp 8126  
VOLUME ["/opt/graphite/conf", "/opt/graphite/storage", "/etc/nginx",
"/opt/statsd", "/etc/logrotate.d", "/var/log"]  
WORKDIR /  
ENV HOME /root  
CMD ["supervisord"]  

