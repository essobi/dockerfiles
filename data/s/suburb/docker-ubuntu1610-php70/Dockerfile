FROM ubuntu:16.10  
# Install apache 2  
RUN apt-get update && \  
apt-get -y install apache2 nano git  
  
# Create html folder  
RUN rm -rf /var/www/html && mkdir -p /var/www/html  
RUN chown www-data:www-data -R /var/www/html  
  
# Add user called suburb  
RUN useradd -ms /bin/bash -G www-data suburb  
RUN usermod -aG sudo suburb  
RUN passwd -d suburb  
  
# Add apache2 env params  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV TERM xterm  
  
# Install PHP 7.0  
RUN apt-get update && \  
apt-get -y install php7.0 gcc make re2c libpcre3-dev libapache2-mod-php7.0
mcrypt php7.0-mcrypt php7.0-mbstring php7.0-json php7.0-dev php7.0-curl
php7.0-mysql php7.0-sqlite php7.0-bcmath  
  
# Enable PHP 7.0  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini  
#RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
# Copy apache cong file with web site configuration to apache folder  
COPY conf/mainwebsite.conf /etc/apache2/sites-available/mainwebsite.conf  
RUN rm -f /etc/apache2/sites-enabled/000-default.conf  
  
# Enable Web site  
RUN a2ensite mainwebsite.conf  
  
# Define workdir  
WORKDIR /var/www/html  
  
# Install Curl  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Clean apt-get files  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose port 80  
EXPOSE 80  
# Start Apache service  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

