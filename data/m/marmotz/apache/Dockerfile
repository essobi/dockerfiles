FROM marmotz/php  
  
USER root  
  
ENV APACHE_RUN_USER nonrootuser  
ENV APACHE_RUN_GROUP nonrootuser  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Apache  
RUN apt-get update -y && apt-get install -y apache2  
RUN a2enmod rewrite  
  
ADD init_apache.sh /  
  
# PHP  
RUN apt-get install -y --force-yes libapache2-mod-php && \  
cp /etc/php/7.0/cli/php.ini /etc/php/7.0/apache2/php.ini  
  
RUN a2enmod php7.0  
  
# Clean  
RUN rm -rf /var/lib/apt/lists/*  
  
USER nonrootuser  
  
VOLUME [ "/var/www", "/var/log/apache2" ]  
WORKDIR /var/www  
  
EXPOSE 80  
CMD ["/init_apache.sh"]  

