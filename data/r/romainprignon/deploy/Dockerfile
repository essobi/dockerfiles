FROM ubuntu:precise  
  
RUN apt-get update  
  
RUN apt-get install -y git-core curl apache2 php5 libapache2-mod-php5
php5-mcrypt php5-curl php5-intl  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
RUN git clone https://github.com/romainPrignon/configfile.git  
RUN cp configfile/default.conf /etc/apache2/sites-enabled/default  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
ADD . /var/www  
  
VOLUME ["/var/www"]  
  
#RUN curl -sS https://getcomposer.org/installer | php  
#RUN mv composer.phar /usr/bin/composer  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]

