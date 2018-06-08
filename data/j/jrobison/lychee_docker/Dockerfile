FROM alpine:3.6  
MAINTAINER Joel Robison <joel@robisons.us>  
  
## Dependancy installation  
RUN apk update  
RUN apk add libressl  
RUN apk add nginx  
RUN apk add supervisor  
RUN apk add php7 php7-fpm  
RUN apk add php7-mysqli php7-imagick php7-gd ttf-dejavu php7-mcrypt php7-json
php7-session php7-exif php7-zip php7-mbstring  
  
## Grab Lychee V3.1.6 for now - more pipeline builds to come later  
RUN wget https://github.com/electerious/Lychee/archive/v3.1.6.tar.gz -O
/tmp/Lychee.tar.gz  
  
## Pre-Configuration items  
RUN mkdir /var/run/php  
RUN mkdir /run/nginx  
RUN mkdir /etc/supervisor.d  
RUN touch /var/log/supervisord.log  
RUN mkdir /control  
RUN chown nginx /var/log/supervisord.log /control  
RUN rm /etc/php7/php-fpm.d/*  
  
### Extract Lychee & set perms  
RUN tar xzf /tmp/Lychee.tar.gz -C /var/www/  
RUN mv /var/www/Lychee-3.1.6 /var/www/lychee  
RUN chown -R nginx:nginx /var/www/lychee  
RUN chown -R nobody /var/www/lychee/uploads /var/www/lychee/data  
  
## Final Configuration items  
### Setup Lychee config  
RUN rm /etc/nginx/conf.d/default.conf  
COPY build/lychee-nginx.conf /etc/nginx/conf.d/  
  
### Setup nginx base config  
COPY build/base-nginx.conf /etc/nginx/nginx.conf  
  
### Setup PHP-FPM config  
COPY build/lychee-php-fpm.conf /etc/php7/php-fpm.d/lychee.conf  
  
### Setup Supervisord (Using this as we need both php-fpm running and nginx) -
know a better way? please let me know  
COPY build/lychee-supervisor.ini /etc/supervisor.d/  
  
### Setup Volumes  
WORKDIR /  
RUN ln -s /var/www/lychee/uploads uploads  
RUN ln -s /var/www/lychee/data data  
  
VOLUME /uploads  
VOLUME /data  
VOLUME /etc/php7/conf.d/  
  
### Expose Port 8080  
EXPOSE 8080  
## Finally, get to the point  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]  

