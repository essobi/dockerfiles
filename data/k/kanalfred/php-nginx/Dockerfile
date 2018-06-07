# Refer:  
# check phpmyadmin example supervisor  
# http://geekyplatypus.com/dockerise-your-php-application-with-nginx-and-
php7-fpm/  
# socket fastcgi_pass config : /usr/local/etc/php-fpm.d/www.conf  
# tuning: http://www.softwareprojects.com/resources/programming/t-optimizing-
nginx-and-php-fpm-for-high-traffic-sites-2081.html  
# SSL generate (non expire):  
# sudo openssl req -x509 -nodes -days -1 -newkey rsa:2048 -keyout
ssl/nginx.key -out ssl/nginx.crt  
# Mount config;  
# site dir: /www/site  
# site config : /etc/nginx/conf.d/*.conf  
# Permission:  
# user: hostadmin uid 1000  
# group: hostadmin gid 1000  
# Build:  
# docker build -t test/php-nginx .  
# Run:  
# docker run --name web1 -p 8001:80 -p 443:443 -v $PWD/web1:/www -d
kanalfred/php-nginx  
# docker run --name php-nginx -p 8080:80 -p 443:443 --tmpfs /etc/nginx/cache
-v $PWD/site:/www -d kanalfred/php-nginx  
FROM php:7.1-fpm  
  
### [Nginx Copy Start] ###  
ENV NGINX_VERSION 1.10.3-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates  
# seperate install statement to resolve nginx'smodule depending nginx package  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
nginx=${NGINX_VERSION}  
# seperate install statement to resolve nginx'smodule depending nginx package  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
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
### [Nginx Copy End] ###  
### Custom ###  
COPY etc /etc/  
COPY config/opcache.ini /usr/local/etc/php/conf.d/  
COPY code /www/site  
  
# user permission  
#https://stackoverflow.com/questions/23544282/what-is-the-best-way-to-manage-
permissions-for-docker-shared-volumes  
RUN groupadd -g 1000 -r hostadmin \  
&& useradd -u 1000 -r -g hostadmin hostadmin \  
&& chown -R hostadmin:hostadmin /www/site \  
&& usermod -a -G nginx hostadmin \  
&& usermod -a -G www-data hostadmin \  
&& usermod -a -G root hostadmin  
  
# php lib & extensions  
RUN apt-get update \  
&& apt-get install -y \  
git zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j "$(nproc)" gd mbstring mysqli pdo pdo_mysql zip
opcache  
#&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
RUN apt-get update \  
&& apt-get install -y supervisor  
  
WORKDIR /www/site  
EXPOSE 80 443 9000  
#USER hostadmin  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

