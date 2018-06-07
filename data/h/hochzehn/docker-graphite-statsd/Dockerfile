FROM phusion/baseimage:0.9.18  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
ENV GRAPHITE_WEB_PATH=/usr/local/src/graphite-web  
ENV WHISPER_PATH=/usr/local/src/whisper  
ENV CARBON_PATH=/usr/local/src/carbon  
ENV STATSD_PATH=/opt/statsd  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y --force-yes --no-install-recommends install \  
vim \  
nginx \  
python-dev \  
python-flup \  
python-pip \  
python-ldap \  
expect \  
gcc \  
git \  
memcached \  
sqlite3 \  
libcairo2 \  
libcairo2-dev \  
python-cairo \  
pkg-config \  
nodejs \  
&& pip install \  
django==1.5.12 \  
python-memcached==1.53 \  
django-tagging==0.3.1 \  
twisted==11.1.0 \  
txAMQP==0.6.2 \  
&& git clone \--depth 1 -b 0.9.15 https://github.com/graphite-
project/graphite-web.git ${GRAPHITE_WEB_PATH} \  
&& rm -rf ${GRAPHITE_WEB_PATH}/.git \  
&& git clone \--depth 1 -b 0.9.15 https://github.com/graphite-
project/whisper.git ${WHISPER_PATH} \  
&& rm -rf ${WHISPER_PATH}/.git \  
&& git clone \--depth 1 -b 0.9.15 https://github.com/graphite-
project/carbon.git ${CARBON_PATH} \  
&& rm -rf ${CARBON_PATH}/.git \  
&& git clone \--depth 1 -b v0.7.2 https://github.com/etsy/statsd.git
${STATSD_PATH} \  
&& rm -rf ${STATSD_PATH}/.git \  
&& apt-get remove -y \  
gcc \  
git \  
python-dev \  
python-pip \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cd ${GRAPHITE_WEB_PATH} && python ./setup.py install \  
&& cd ${WHISPER_PATH} && python ./setup.py install \  
&& cd ${CARBON_PATH} && python ./setup.py install  
  
# configure graphite  
ADD conf/opt/graphite/conf/*.conf /opt/graphite/conf/  
ADD conf/opt/graphite/webapp/graphite/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py  
  
# configure statsd  
ADD conf/opt/statsd/config.js ${STATSD_PATH}/config.js  
  
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
ADD conf /etc/graphite-statsd/conf  
ADD conf/etc/my_init.d/01_conf_init.sh /etc/my_init.d/01_conf_init.sh  
  
# defaults  
EXPOSE 80 2003-2004 2023-2024 8125/udp 8126  
VOLUME ["/opt/graphite/conf", "/opt/graphite/storage", "/etc/nginx",
"/opt/statsd", "/etc/logrotate.d", "/var/log"]  
WORKDIR /  
ENV HOME /root  
CMD ["/sbin/my_init"]  

