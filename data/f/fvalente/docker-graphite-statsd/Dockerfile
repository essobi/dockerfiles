FROM phusion/baseimage:0.9.21  
ENV PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/"  
RUN apt-get -y update  
  
RUN apt-get install -y nginx \  
python-dev \  
python-flup \  
python-ldap \  
expect \  
sqlite3 \  
libcairo2 \  
libcairo2-dev \  
python-cairo \  
python-rrdtool\  
pkg-config\  
nodejs\  
memcached \  
libffi-dev \  
build-essential \  
vim \  
python \  
python-pip \  
git  
  
RUN pip install django==1.5 django-tagging==0.3.1 pytz txamqp gunicorn python-
memcached  
RUN pip install --no-binary=:all: https://github.com/graphite-
project/whisper/archive/0.9.15.tar.gz  
RUN pip install --no-binary=:all: https://github.com/graphite-
project/carbon/archive/0.9.15.tar.gz  
RUN pip install --no-binary=:all: https://github.com/graphite-
project/graphite-web/archive/0.9.15.tar.gz  
  
ADD conf/opt/graphite/conf/*.conf /opt/graphite/conf/  
ADD conf/opt/graphite/webapp/graphite/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py  
ADD conf/opt/graphite/webapp/graphite/app_settings.py
/opt/graphite/webapp/graphite/app_settings.py  
  
RUN mv /opt/graphite/conf/graphite.wsgi.example
/opt/graphite/webapp/graphite/graphite_wsgi.py  
  
# config nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD conf/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD conf/etc/nginx/sites-enabled/graphite-statsd.conf /etc/nginx/sites-
enabled/graphite-statsd.conf  
  
# install statsd  
RUN git clone -b v0.7.2 https://github.com/etsy/statsd.git /opt/statsd  
ADD conf/opt/statsd/config.js /opt/statsd/config.js  
  
ADD conf/usr/local/bin/django_admin_init.exp
/usr/local/bin/django_admin_init.exp  
RUN /usr/local/bin/django_admin_init.exp  
  
# logging support  
RUN mkdir -p /var/log/carbon /var/log/graphite /var/log/nginx  
ADD conf/etc/logrotate.d/graphite-statsd /etc/logrotate.d/graphite-statsd  
  
# daemons  
ADD conf/etc/service/carbon/run /etc/service/carbon/run  
ADD conf/etc/service/carbon-aggregator/run /etc/service/carbon-aggregator/run  
ADD conf/etc/service/graphite/run /etc/service/graphite/run  
ADD conf/etc/service/statsd/run /etc/service/statsd/run  
ADD conf/etc/service/nginx/run /etc/service/nginx/run  
  
# default conf setup  
ADD conf /etc/graphite-statsd/conf  
ADD conf/etc/my_init.d/01_conf_init.sh /etc/my_init.d/01_conf_init.sh  
  
# # cleanup  
RUN apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# # defaults  
EXPOSE 80 2003-2004 2023-2024 8125/udp 8126  
VOLUME ["/opt/graphite/conf", "/opt/graphite/storage", "/etc/nginx",
"/opt/statsd", "/etc/logrotate.d", "/var/log"]  
WORKDIR /  
ENV HOME /root  
CMD ["/sbin/my_init"]  

