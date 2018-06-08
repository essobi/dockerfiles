FROM prestashop/prestashop:1.7.3.0  
  
MAINTAINER Lukas Cerny <lukas.cerny@futuretek.cz>  
  
# Add memcached  
RUN apt-get update \  
&& apt-get install -y libmemcached11 libmemcachedutil2 build-essential
libmemcached-dev libz-dev cron wget \  
&& pecl install memcached-2.2.0 \  
&& echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini \  
&& apt-get remove -y build-essential libmemcached-dev libz-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/pear  
  
COPY ./etc /etc  
  
RUN sed -i 's|#!/bin/sh|#!/bin/sh\ncron;\nln -sf /root/cron/crontab
/etc/crontab;|g' /tmp/docker_run.sh \  
&& mkdir /root/cron \  
&& touch /etc/crontab  

