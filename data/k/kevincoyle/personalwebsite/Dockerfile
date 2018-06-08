FROM drupal:8.1.0-apache  
  
#Copy the settings file  
COPY ./app/settings/settings.php /var/www/html/sites/default/settings.php  
  
# Drush installation  
RUN apt-get update -y  
RUN apt-get install wget -y  
RUN apt-get install mysql-client -y  
RUN wget http://files.drush.org/drush-unstable.phar  
RUN chmod +x drush-unstable.phar  
RUN mv drush-unstable.phar /usr/local/bin/drush  
  
# Composer  
RUN wget https://getcomposer.org/composer.phar  
RUN chmod +x composer.phar  
RUN mv composer.phar /usr/local/bin/composer  
# Drupal Console  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar  
RUN mv drupal.phar /usr/local/bin/drupal  
RUN chmod +x /usr/local/bin/drupal  
  
RUN apt-get install netcat -y  
  
#SENDMAIL  
RUN apt-get install sendmail -y  
RUN echo "sendmail_path = /usr/sbin/sendmail -t -i" >>
/usr/local/etc/php/php.ini  
COPY ./app/modules /var/www/html/modules  
RUN php /var/www/html/modules/composer_manager/scripts/init.php  
RUN cd /var/www/html && composer drupal-update  
RUN cd /var/www/html && composer dump-autoload  

