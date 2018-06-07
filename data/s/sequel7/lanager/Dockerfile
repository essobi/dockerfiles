FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install the project's packaged dependencies  
RUN apt-get update && \  
apt-get -y install git php5-common php5-cli php5-mcrypt php5-curl php5-mysql
libapache2-mod-php5 mysql-server apache2 curl  
  
# Enable Apache and PHP modules  
RUN a2enmod rewrite  
RUN php5enmod mcrypt curl  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
# Clone the project  
RUN git clone https://github.com/zeropingheroes/lanager.git /var/www/lanager  
  
# Install the project's dependencies  
WORKDIR /var/www/lanager  
RUN composer update  
  
# Configure Apache to use the LANager's public directory as the web root  
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Allow full read and write access on the app's storage directory  
RUN chmod -R 777 /var/www/lanager/app/storage  
  
# Create a MySQL user and database and grant the required privileges  
RUN service mysql start && \  
echo "CREATE DATABASE lanager; CREATE USER 'lanager'@'localhost' IDENTIFIED BY
'lanager'; GRANT ALL PRIVILEGES ON lanager.* TO 'lanager'@'localhost'; FLUSH
PRIVILEGES;" | mysql -u root  
  
# Set the correct time zone for your location in the app config file  
RUN cat /var/www/lanager/app/config/app.php | sed
s/"Europe\/London"/"America\/New_York"/ > /tmp/app.php && \  
mv /tmp/app.php /var/www/lanager/app/config/app.php  
  
# Get going  
WORKDIR /var/www/lanager  
COPY start.sh /start.sh  
ENTRYPOINT /start.sh  

