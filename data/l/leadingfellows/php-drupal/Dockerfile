FROM wodby/php:5.6  
  
USER root  
  
RUN set -ex && \  
su-exec www-data composer global require drush/drush && \  
su-exec www-data composer clear-cache && \  
su-exec www-data drush cc drush && \  
curl https://drupalconsole.com/installer -L -o drupal.phar && \  
mv drupal.phar /usr/local/bin/drupal && \  
chmod +x /usr/local/bin/drupal  
  
USER www-data  

