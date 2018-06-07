FROM djpable/drupal-dev  
MAINTAINER Paolo Mazzoni <ing.paolo.mazzoni@gmail.com>  
  
# Increase PHP memory limit (from 128MB)  
RUN echo "memory_limit=512M" > /usr/local/etc/php/conf.d/docker-php.ini  
  
# Specific .htaccess settings  
RUN echo "" >> /var/www/html/.htaccess  
RUN echo "# *** CUSTOM ***" >> /var/www/html/.htaccess  
RUN echo "<IfModule mod_php5.c>" >> /var/www/html/.htaccess  
RUN echo " php_value max_execution_time 240" >> /var/www/html/.htaccess  
#RUN echo " php_value memory_limit 2048M" >> /var/www/html/.htaccess  
RUN echo " php_value apc.rfc1867 1" >> /var/www/html/.htaccess  
RUN echo " php_value max_input_vars 5000" >> /var/www/html/.htaccess  
RUN echo " php_value max_input_time 120" >> /var/www/html/.htaccess  
RUN echo " php_value upload_max_filesize 10M" >> /var/www/html/.htaccess  
RUN echo "</IfModule>" >> /var/www/html/.htaccess  
  
# (*) Create directories for Drupal  
RUN mkdir /tmp/drupal  
RUN chown -R www-data:www-data /tmp/drupal  
RUN mkdir /var/www/private  
RUN chown -R www-data:www-data /var/www/private  
  
# "sites" folder download from GIT repository  
#RUN rm -r sites  
#RUN git clone
https://djpable:X6GVMEmR@bitbucket.org/it3xp3rt/ordingpg/ordingpg ./sites  
#RUN chown -R www-data:www-data sites  
# Specific settings  
#COPY files/settings.php /var/www/html/sites/default/  
#RUN chown -R www-data:www-data /var/www/html/sites/default/settings.php  
# Copy specific scripts  
#COPY files/aliases.drushrc.php /root/.drush/aliases.drushrc.php  
#COPY files/after_sync.sh /root/after_sync.sh

