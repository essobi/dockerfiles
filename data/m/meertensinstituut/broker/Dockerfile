FROM ubuntu:16.04  
MAINTAINER Matthijs Brouwer, Meertens Institute  
  
EXPOSE 80  
USER root  
  
WORKDIR "/root"  
  
RUN mkdir lib  
  
RUN apt-get update && apt-get install -y locales apache2 libapache2-mod-php
php php-cli php-curl curl php-sqlite3 sqlite3 php-mbstring subversion git vim
&& \  
locale-gen en_US.UTF-8 en_US && update-locale LANG=en_US.UTF-8
LANGUAGE=en_US:en  
  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');" && \  
php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
&& \  
rm -rf /tmp/composer-setup.php  
  
RUN service apache2 stop && \  
echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && \  
a2enconf fqdn && \  
rm -rf /var/www/html/* && \  
printf "echo\n" >> /start.sh && \  
printf "echo \"=============================== BROKER
================================\"\n" >> /start.sh && \  
printf "echo \" See https://meertensinstituut.github.io/broker/ for more
information\"\n" >> /start.sh && \  
printf "echo
\"=======================================================================\"\n"
>> /start.sh && \  
printf "echo\n" >> /start.sh && \  
printf "service apache2 start\n" >> /start.sh && \  
chmod 755 /start.sh  
  
RUN svn --force export https://github.com/meertensinstituut/broker/trunk/src/
/var/www/html && \  
chmod 777 /var/www/html/cache && \  
composer install -d /var/www/html/  
  
CMD bash -C '/start.sh'; 'bash'

