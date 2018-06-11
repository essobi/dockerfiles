# Modified drupal image  
FROM drupal:latest  
  
MAINTAINER Andre Fernandes <andre@vertigo.com.br>  
  
RUN curl http://drupalconsole.com/installer -L -o drupal.phar && \  
mv drupal.phar /usr/local/bin/drupal && chmod +x /usr/local/bin/drupal && \  
drupal init  
RUN echo "display_errors = On" > /usr/local/etc/php/conf.d/vtg-custom.ini  
RUN php -r "readfile('http://files.drush.org/drush.phar');" > drush && \  
chmod +x drush && \  
mv drush /usr/local/bin/ && \  
drush init -y && \  
echo "source /root/.drush/drush.bashrc" >> ~/.bashrc && \  
echo "source /root/.drush/drush.complete.sh" >> ~/.bashrc && \  
echo "source /root/.drush/drush.prompt.sh" >> ~/.bashrc  
RUN drush si standard --db-url=sqlite://sites/default/files/.ht.sqlite
--account-pass=senha --locale=pt-br -y && \  
chown -R www-data:www-data /var/www/html/sites  
# themes, modules etc. will be  
# overriden by mount point  
RUN drush dl bootstrap  

