FROM ubuntu:trusty  
  
# Set environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get update  
RUN apt-get -y install supervisor git pwgen apache2 libapache2-mod-php5
php5-mysql php-apc php5-mcrypt mysql-client  
  
# Prepare scripts  
RUN mkdir -p /scripts  
ADD scripts/start-apache2.sh /scripts/start-apache2.sh  
ADD scripts/run.sh /scripts/run.sh  
RUN chown -Rf root:root /scripts  
RUN chmod -Rf 755 /scripts  
  
# Prepare configuration files and enable .htaccess  
ADD configs/supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-
apache2.conf  
ADD configs/apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Configure /app folder  
RUN mkdir -p /app && rm -rf /var/www/html && ln -s /app /var/www/html  
  
# Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Expose the http port  
EXPOSE 80  
# Run the initial script  
CMD ["/scripts/run.sh"]  

