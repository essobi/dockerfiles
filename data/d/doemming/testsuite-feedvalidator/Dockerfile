FROM ubuntu:14.04  
MAINTAINER bespire UG  
# based on https://hub.docker.com/r/unboxed/docker-feed-validator/  
# and http://feedvalidator.org/docs/howto/install_and_run.html  
# and https://medium.com/dev-tricks/apache-and-php-on-docker-44faef716150  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install apache2-mpm-worker git python \  
&& apt-get clean  
  
RUN rm -rf /var/www/html  
  
RUN git clone https://github.com/bor8/feedvalidator.git /var/www/feedvalidator
\  
&& cd /var/www/feedvalidator \  
&& git checkout tags/2016-10-27  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
ADD resources/apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN a2enmod cgi rewrite  
  
EXPOSE 80  
CMD ls -la /var/run/apache2 \  
&& rm -f /var/run/apache2/apache2.pid \  
&& rm -f /var/run/apache2/cgisock.* \  
&& service apache2 start \  
&& sleep infinity  
# CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
# && /usr/sbin/apache2ctl -D FOREGROUND

