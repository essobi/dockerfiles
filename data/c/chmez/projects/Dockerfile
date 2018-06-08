# Download OS image  
FROM ubuntu:16.10  
# Update packages  
RUN apt-get update  
  
# Install and configure Apache2 web server  
RUN apt-get install -y apache2  
RUN echo "\nServerName 127.0.0.1\n" >> /etc/apache2/apache2.conf  
  
# Install and configure MySQL 5.7 database server  
ENV DEBIAN_FRONTEND=noninteractive  
RUN echo "mysql-server-5.7 mysql-server/root_password password root" |
debconf-set-selections  
RUN echo "mysql-server-5.7 mysql-server/root_password_again password root" |
debconf-set-selections  
RUN apt-get install -y mysql-server-5.7  
RUN usermod -d /usr/lib/mysql mysql  
  
# Install PHP 7.0 and extensions  
RUN apt-get install -y php7.0 libapache2-mod-php7.0 php7.0-mysql  
  
# Install Drush 8  
RUN apt-get install -y php7.0-zip php7.0-xml curl  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN composer global require drush/drush:8.*  
  
# Preparing web server for install Drupal  
RUN apt-get install -y php7.0-gd sendmail  
COPY 000-default.conf /etc/apache2/sites-available  
RUN a2enmod rewrite  
RUN a2enmod headers  
ENV PATH="/root/.composer/vendor/bin:${PATH}"  
WORKDIR /var/www/html  
  
# Download site files from repository  
RUN rm -rf *  
RUN apt-get install -y git wget  
RUN git clone https://github.com/chmez/portfolio.git .  
RUN wget https://ftp.drupal.org/files/projects/drupal-8.1.10.tar.gz  
RUN tar zxfv drupal-8.1.10.tar.gz  
RUN mv drupal-8.1.10/vendor .  
RUN mv drupal-8.1.10/core/assets core  
RUN rm -rf drupal-8.1.10*  
  
# Sync site root directory with local machine  
VOLUME "/var/www/html"  
  
CMD tail -f /dev/null

