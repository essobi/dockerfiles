FROM ubuntu:latest  
MAINTAINER Markus Kosmal <mko@bebrand.de>  
  
# settings:apache  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# settings:db  
ENV DATABASE_DRIVER sqlite  
ENV DATABASE_USER root  
ENV DATABASE_PW ""  
ENV DATABASE_HOST localhost  
ENV DATABASE_NAME kanboard  
  
# packages  
RUN apt-get update \  
&& apt-get install -y nano apache2 php5 php5-sqlite git curl \  
&& apt-get clean  
  
# bind to localhost  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# get composer  
RUN curl -sS https://getcomposer.org/installer | php --
--filename=/usr/local/bin/composer  
  
# kanboard setup  
RUN cd /var/www \  
&& git clone https://github.com/fguillot/kanboard.git \  
&& cd /var/www/kanboard \  
&& composer install \  
&& rm -rf /var/www/html \  
&& mv /var/www/kanboard /var/www/html \  
&& chown -R www-data:www-data /var/www/html/data  
  
# db customization  
ADD ./bootstrap/db_handler.sh /var/www/html/db.sh  
RUN chmod a+x /var/www/html/db.sh \  
&& cd /var/www/html \  
&& sh ./db.sh \  
&& rm -f ./db.sh  
  
# default client assets  
ADD ./assets/* /var/www/html/assets/  
  
# provision  
EXPOSE 80  
VOLUME ["/var/www/html/data","/var/www/html/assets"]  
  
# bootstrap  
CMD /usr/sbin/apache2ctl -D FOREGROUND

