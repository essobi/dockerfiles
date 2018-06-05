FROM phusion/baseimage:0.9.18  
  
CMD ["/sbin/my_init"]  
  
RUN export LANG=en_US.utf8 && add-apt-repository ppa:ondrej/php -y  
RUN apt-get update && apt-get install -y apache2 php5.6 php5.6-curl
php5.6-mysql php5.6-gd php5.6-xml php5.6-imap php5.6-soap  
RUN a2enmod rewrite ;\  
a2enmod ssl ;\  
a2enmod remoteip;\  
mkdir /etc/service/apache2  
ADD apache2.sh /etc/service/apache2/run  
ADD whmcs.sh /etc/service/whmcs/run  
RUN chmod +x /etc/service/apache2/run ;\  
chown root:root /etc/service/apache2/run ;\  
chmod +x /etc/service/whmcs/run ;\  
chown root:root /etc/service/whmcs/run  
  
RUN curl
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
| tar xvz ;\  
cp /ioncube/ioncube_loader_lin_5.6.so /usr/lib/php/20131226/ ;\  
rm -rf /ioncube/ ;\  
echo "zend_extension=ioncube_loader_lin_5.6.so" > /etc/php/5.6/mods-
available/ioncube.ini ;\  
ln -s /etc/php/5.6/mods-available/ioncube.ini
/etc/php/5.6/apache2/conf.d/01-ioncube.ini ;\  
ln -s /etc/php/5.6/mods-available/ioncube.ini
/etc/php/5.6/cli/conf.d/01-ioncube.ini  
  
ADD run.sh /var/www/run.sh  
ADD src /var/www/public  
WORKDIR /var/www/public  
RUN mkdir /var/www/secured ;\  
mv /var/www/public/crons /var/www/secured ;\  
mv /var/www/public/attachments /var/www/secured ;\  
mv /var/www/public/templates_c /var/www/secured ;\  
mv /var/www/public/downloads /var/www/secured ;\  
mv /var/www/public/htaccess.txt /var/www/public/.htaccess ;\  
mv /var/www/public/install /var/www/install ;\  
rm /var/www/public/configuration.php.new ;\  
chown -R www-data:www-data /var/www ;\  
chmod +x /var/www/run.sh  
  
RUN echo "MAILTO=''\n\n10 23 * * * php -q /var/www/secured/crons/cron.php
>>/var/log/syslog 2>&1 /\n0 */4 * * * php -q
/var/www/secured/crons/domainsync.php >>/var/log/syslog 2>&1 \n*/5 * * * * php
-q /var/www/secured/crons/pipe.php >>/var/log/syslog 2>&1 \n*/5 * * * * php -q
/var/www/secured/crons/pop.php >>/var/log/syslog 2>&1" > cronJob ;\  
crontab cronJob ;\  
rm cronJob  
  
ENV LICENSE_KEY= ENCRYPT_HASH= LICENSED_PUBLIC_IP= MYSQL_DB_HOST=localhost
MYSQL_USERNAME=username MYSQL_PASSWORD=pass MYSQL_DB_NAME=db_name  
ENV APACHE_RUN_USER=www-data APACHE_RUN_GROUP=www-data
APACHE_PID_FILE=/var/run/apache2/apache2.pid APACHE_RUN_DIR=/var/lock/apache2
APACHE_LOCK_DIR=/var/lock/apache2 APACHE_LOG_DIR=/var/log/apache2  
  
VOLUME ["/var/www/secured/attachments", "/var/www/secured/downloads",
"/var/www/languages", "/var/www/modules"]  
  
EXPOSE 80 443  
  
ADD configuration.php /var/www/public/configuration.php  
ADD cron.config.php /var/www/secured/crons/config.php  
ADD site.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

