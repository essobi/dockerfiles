FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND="noninteractive"  
# Install utilities and LAMP stack.  
RUN apt-get update && \  
echo "mysql-server-5.5 mysql-server/root_password password root" | debconf-
set-selections && \  
echo "mysql-server-5.5 mysql-server/root_password_again password root" |
debconf-set-selections && \  
apt-get install wget git nano curl apache2 mysql-server-5.5 php5-mysql php5
php5-cli php5-gd php5-curl libapache2-mod-php5 php5-mcrypt -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y  
  
# Install composer.  
RUN EXPECTED_SIGNATURE=$(wget -q -O -
https://composer.github.io/installer.sig) && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'${EXPECTED_SIGNATURE}') { echo 'Installer verified'; } else { echo 'Installer
corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
ENV PATH=~/.composer/vendor/bin:$PATH  
  
# Install drush.  
RUN composer global require drush/drush:8.1.11  
  
# Define working directory.  
WORKDIR /var/www/html  
  
# Copy conf files.  
COPY conf/000-default.conf 000-default.conf  
  
# Start container.  
COPY startup.sh startup.sh  
CMD ["/bin/bash", "startup.sh"]  

