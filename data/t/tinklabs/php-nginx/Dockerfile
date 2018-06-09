FROM tinklabs/php:5.6-fpm  
  
# Install nginx  
# ENV NGINX_VERSION 1.11.9-1~jessie  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install supervisor and common tools  
RUN apt-get update \  
&& apt-get install -y supervisor vim zip unzip git net-tools  
  
# Copy config files  
RUN rm -Rf /etc/nginx/nginx.conf  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
ADD supervisor/supervisord-nginx.conf /etc/supervisor/supervisord.conf  
ADD ./php/php-fpm.d/www.conf /usr/local/etc/php-fpm.conf  
  
# Install php composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Clean up the rubbish  
RUN apt-get autoremove -y \  
&& apt-get clean \  
&& apt-get remove -y build-essential libmemcached-dev libz-dev \  
&& rm -rf /tmp/pear \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 443 80  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

