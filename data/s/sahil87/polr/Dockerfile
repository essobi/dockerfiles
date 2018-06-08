FROM php:7.1-fpm  
  
#Install php extensions  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libxslt-dev \  
libffi-dev \  
libpq-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt pdo_mysql mysqli exif intl
xsl json soap dom zip\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
#START NGINX install from https://github.com/nginxinc/docker-
nginx/blob/master/mainline/jessie/Dockerfile  
ENV NGINX_VERSION 1.13.3-1~jessie  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
#END NGINX install  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#Install other dependencies  
RUN apt-get update \  
&& apt-get install -y emacs-nox git sudo supervisor  
  
#Polr files  
COPY . /src  
COPY docker_related/ /  
  
RUN cd /src && \  
composer install -n -d /src && \  
chown -R nginx:nginx /src  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "-n", "-c", "/supervisord.conf"]  

