FROM ubuntu:14.04  
  
MAINTAINER schmorrison <schmorrison@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
#RUN echo 'Acquire::http { Proxy "http://172.17.0.2:3142"; };' >>
/etc/apt/apt.conf.d/01proxy  
  
RUN apt-get update && apt-get install -y \  
curl \  
expect \  
git \  
language-pack-en-base \  
mysql-server \  
nano \  
redis-server \  
screen \  
supervisor \  
software-properties-common \  
wget \  
&& export LC_ALL=en_US.UTF-8 \  
&& export LANG=en_US.UTF-8 \  
&& add-apt-repository ppa:ondrej/php5-5.6 -y \  
&& apt-get update && apt-get install -y \  
apache2 \  
php5 \  
php5-cli \  
php5-mcrypt \  
php5-intl \  
php5-mysql \  
php5-curl \  
php5-gd  
  
ADD /static /root/  
  
RUN MYSQL_ROOT_PASS=$(echo -e `date` | md5sum | awk '{ print $1 }') \  
&& sleep 1 \  
&& SEAT_DB_PASS=$(echo -e `date` | md5sum | awk '{ print $1 }') \  
&& echo "MySQL $MYSQL_ROOT_PASS" > /root/seat-install-creds \  
&& echo "User $SEAT_DB_PASS" >> /root/seat-install-creds \  
&& /etc/init.d/mysql start \  
&& mysqladmin -u root password "$MYSQL_ROOT_PASS" \  
&& mysql -u root -p$MYSQL_ROOT_PASS -e "CREATE DATABASE seat;" \  
&& mysql -u root -p$MYSQL_ROOT_PASS -e "GRANT ALL ON seat.* to seat@localhost
IDENTIFIED BY '$SEAT_DB_PASS';" \  
&& cd /var/www \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& hash -r \  
&& composer create-project eveseat/seat seat --keep-vcs --prefer-source \--no-
dev \  
&& chown -R www-data:www-data /var/www/seat \  
&& chmod -R guo+w /var/www/seat/storage/ \  
&& cd /var/www/seat \  
&& sed -i -r "s/DB_DATABASE=homestead/DB_DATABASE=seat/" /var/www/seat/.env \  
&& sed -i -r "s/DB_USERNAME=homestead/DB_USERNAME=seat/" /var/www/seat/.env \  
&& sed -i -r "s/DB_PASSWORD=secret/DB_PASSWORD=$SEAT_DB_PASS/"
/var/www/seat/.env \  
&& sed -i -r "s/CACHE_DRIVER=file/CACHE_DRIVER=redis/" /var/www/seat/.env \  
&& sed -i -r "s/QUEUE_DRIVER=sync/QUEUE_DRIVER=redis/" /var/www/seat/.env \  
&& sed -i -r "s/Options Indexes FollowSymLinks/Options FollowSymLinks/"
/etc/apache2/apache2.conf \  
&& sed -i -r "s/ServerTokens OS/ServerTokens Prod/" /etc/apache2/conf-
enabled/security.conf \  
&& sed -i -r "s/ServerSignature On/ServerSignature Off/" /etc/apache2/conf-
enabled/security.conf \  
&& php artisan vendor:publish \  
&& php artisan migrate \  
&& php artisan db:seed
\--class=Seat\\\Services\\\database\\\seeds\\\NotificationTypesSeeder \  
&& php artisan db:seed
\--class=Seat\\\Services\\\database\\\seeds\\\ScheduleSeeder \  
&& php artisan eve:update-sde -n \  
&& mv /root/seat.conf /etc/supervisor/conf.d/seat.conf \  
&& mv /root/100-seat.local.conf /etc/apache2/sites-
available/100-seat.local.conf  
  
RUN touch /root/seatup.sh && chmod +x /root/seatup.sh \  
&& echo "#!/bin/bash" >> /root/seatup.sh \  
&& echo "cd /var/www/seat" >> /root/seatup.sh \  
&& echo "service mysql start && redis-server --daemonize yes" >>
/root/seatup.sh \  
&& echo "php artisan seat:admin:reset" >> /root/seatup.sh \  
&& echo "php artisan seat:admin:email" >> /root/seatup.sh \  
&& touch /root/startup.sh && chmod +x /root/startup.sh \  
&& echo "#!/bin/bash" >> /root/startup.sh \  
&& echo "status=$(ps -ef | grep -v grep | grep supervisor | wc -l)" >>
/root/startup.sh \  
&& echo "if [$status = 0]" >> /root/startup.sh \  
&& echo "then" >> /root/startup.sh \  
&& echo "service start supervisor && supervisorctl reload" >> /root/startup.sh
\  
&& echo "fi" >> /root/startup.sh \  
&& echo "status=$(ps -ef | grep -v grep | grep mysql | wc -l)" >>
/root/startup.sh \  
&& echo "if [$status = 0]" >> /root/startup.sh \  
&& echo "then" >> /root/startup.sh \  
&& echo "service start mysql" >> /root/startup.sh \  
&& echo "fi" >> /root/startup.sh \  
&& echo "status=$(redis-cli ping)" >> /root/startup.sh \  
&& echo "if [$status = "PONG"]" >> /root/startup.sh \  
&& echo "then" >> /root/startup.sh \  
&& echo "redis-server --daemonize yes" >> /root/startup.sh \  
&& echo "fi" >> /root/startup.sh \  
&& echo "status=$(ps -ef | grep -v grep | grep apache2 | wc -l)" >>
/root/startup.sh \  
&& echo "if [$status = 0]" >> /root/startup.sh \  
&& echo "then" >> /root/startup.sh \  
&& echo "service start apache2 && apachectl restart" >> /root/startup.sh \  
&& echo "fi" >> /root/startup.sh \  
&& unlink /etc/apache2/sites-enabled/000-default.conf \  
&& ln -s /var/www/seat/public /var/www/html/eve.schmorrison.tk \  
&& ln -s /etc/apache2/sites-available/100-seat.local.conf /etc/apache2/sites-
enabled/100-seat.local.conf  
  
  
RUN /etc/init.d/mysql start \  
&& crontab /root/crontab \  
&& a2enmod rewrite \  
&& service apache2 restart \  
&& apachectl restart \  
&& apachectl -t -D DUMP_VHOSTS  
  
EXPOSE 80  
CMD /bin/bash  

