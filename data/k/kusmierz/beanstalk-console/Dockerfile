FROM php:7.1-alpine  
MAINTAINER Adam Kusmierz <adam@kusmierz.be>  
  
## Add the files  
ADD php.ini /usr/local/etc/php/conf.d/php.ini  
  
## Add Tini  
RUN apk add --update --no-cache tini  
ENTRYPOINT ["/sbin/tini", "--"]  
  
## install adminer and default theme  
ENV BEANSTALK_CONSOLE_VERSION 1.7.6  
ADD
https://github.com/ptrofimov/beanstalk_console/archive/$BEANSTALK_CONSOLE_VERSION.tar.gz
/tmp/$BEANSTALK_CONSOLE_VERSION.tar.gz  
RUN tar xvz -C /tmp/ -f /tmp/$BEANSTALK_CONSOLE_VERSION.tar.gz \  
&& mv /tmp/beanstalk_console-$BEANSTALK_CONSOLE_VERSION/ /var/www \  
&& chown www-data:www-data -R /var/www \  
&& rm /tmp/$BEANSTALK_CONSOLE_VERSION.tar.gz  
  
## Expose the port  
EXPOSE 80  
CMD php -S 0.0.0.0:80 -t /var/www/public/  

