FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
RUN apk add -U php5-fpm  
  
## listen [::]:9000  
COPY tmpl/_etc_php5_php-fpm.conf.tmpl /etc/php5/php-fpm.conf.tmpl  
  
RUN mkdir -p /var/www/html  
  
VOLUME /var/www/html  
  
EXPOSE 9000  
#todo log  
## --nodaemonize  
CMD ["dockerize", "-template","/etc/php5/php-fpm.conf.tmpl:/etc/php5/php-
fpm.conf","php-fpm","-F"]  
  

