FROM node:8.11-slim  
  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV PATH
/usr/src/app/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
git \  
nginx \  
php-apc \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-memcached \  
php5-mcrypt \  
php5-mysql \  
unzip \  
&& apt-get purge -y --auto-remove \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
RUN rm -f /etc/nginx/conf.d/default.conf \  
&& rm -f /etc/nginx/sites-enabled/default \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
WORKDIR /usr/src/app  
  
COPY conf/nginx.conf /etc/nginx/nginx.conf  
COPY conf/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
  
CMD nginx -t && service nginx start && php5-fpm -F  

