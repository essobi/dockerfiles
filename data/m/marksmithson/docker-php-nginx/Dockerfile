FROM ubuntu:14.04  
MAINTAINER Mark Smithson mark@digital-morphosis.com  
RUN apt-get update  
RUN apt-get upgrade -y  
ENV REFRESHED_AT 2014-10-21  
# PHP  
RUN apt-get install -y supervisor php5-cli php5-curl php5-fpm php5-gd
php5-mcrypt php5-mysql  
RUN php5enmod mcrypt  
  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /var/run/php5-fpm  
RUN mkdir -p /data/logs/nginx  
RUN mkdir -p /data/www  
  
# NGINX  
RUN apt-get install -y nginx  
  
COPY docker/nginx.conf /etc/nginx/nginx.conf  
COPY docker/default-site /etc/nginx/sites-available/default  
COPY docker/php.conf /etc/supervisor/conf.d/php.conf  
COPY docker/start.sh /start.sh  
  
# COPY info.php /data/www/info.php  
RUN sed -i "s/;daemonize.*/daemonize = no/g" /etc/php5/fpm/php-fpm.conf  
  
RUN apt-get install -y python-setuptools  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
RUN /usr/bin/easy_install supervisor-stdout  
  
EXPOSE 80  
ENTRYPOINT ["/start.sh"]

