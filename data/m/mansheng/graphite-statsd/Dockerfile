FROM phusion/baseimage:0.9.19  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
# dependencies  
RUN apt-get -y update && apt-get -y --force-yes install\  
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
pkg-config\  
nodejs\  
&& rm -rf /var/lib/apt/lists/*  
  
# python dependencies  
RUN pip install django==1.5.12\  
python-memcached==1.53\  
django-tagging==0.3.1\  
twisted==11.1.0\  
txAMQP==0.6.2  
  
# install graphite  
RUN git clone -b 0.9.15 --depth 1 https://github.com/graphite-
project/graphite-web.git /usr/local/src/graphite-web  
WORKDIR /usr/local/src/graphite-web  
RUN python ./setup.py install  
ADD conf/opt/graphite/conf/*.conf /opt/graphite/conf/  
ADD conf/opt/graphite/webapp/graphite/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py  
  
# install whisper  
RUN git clone -b 0.9.15 --depth 1 https://github.com/graphite-
project/whisper.git /usr/local/src/whisper  
WORKDIR /usr/local/src/whisper  
RUN python ./setup.py install  
  
# install carbon  
RUN git clone -b 0.9.15 --depth 1 https://github.com/graphite-
project/carbon.git /usr/local/src/carbon  
WORKDIR /usr/local/src/carbon  
RUN python ./setup.py install  
  
# install statsd  
RUN git clone -b v0.8.0 https://github.com/etsy/statsd.git /opt/statsd  
ADD conf/opt/statsd/config.js /opt/statsd/config.js  
  
# config nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD conf/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD conf/etc/nginx/sites-enabled/graphite-statsd.conf /etc/nginx/sites-
enabled/graphite-statsd.conf  
  
# init django admin  
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
ADD conf/etc/my_init.d/01_conf_init.sh /etc/my_init.d/01_conf_init.sh  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/local/src  
  
# defaults  
VOLUME ["/opt/graphite/storage"]  
WORKDIR /  
ENV HOME /root  
CMD ["/sbin/my_init"]  

