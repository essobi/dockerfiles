FROM phusion/baseimage:latest  
MAINTAINER sensei73 <sensei73@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
#Apache+php  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -y install git apache2 php5 php5-curl php5-gd php5-gmp php5-mysql \  
&& apt-get -y clean \  
&& sed -i "s/^;date.timezone =.*/date.timezone = Europe\/Paris/"
/etc/php5/*/php.ini \  
  
#add spotweb  
&& rm -r /var/www/html \  
  
# Enable php rewrite  
&& a2enmod rewrite  
  
# Update apache configuration  
ADD apache-config.conf /etc/apache2/sites-available/000-default.conf  
  
# Manually set the apache environment variables in order to get apache to work
immediately.  
RUN echo www-data > /etc/container_environment/APACHE_RUN_USER \  
&& echo www-data > /etc/container_environment/APACHE_RUN_GROUP \  
&& echo /var/log/apache2 > /etc/container_environment/APACHE_LOG_DIR \  
&& echo /var/lock/apache2 > /etc/container_environment/APACHE_LOCK_DIR \  
&& echo /var/run/apache2.pid > /etc/container_environment/APACHE_PID_FILE  
  
#Install & run Cron  
ADD cron /root/cron  
ADD script.sh /root/script.sh  
RUN chmod +x /root/script.sh \  
&& apt-get install cron -y \  
&& crontab /root/cron \  
&& cron \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
EXPOSE 80  
# Add firstrun.sh to execute during container startup  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add apache to runit  
RUN mkdir /etc/service/apache  
ADD apache.sh /etc/service/apache/run  
RUN chmod +x /etc/service/apache/run  

