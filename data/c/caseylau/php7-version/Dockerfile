FROM caseylau/php7-extension:oci8  
ENV DRUSH_VERSION 0.4.2  
# drush command  
RUN curl -fsSL -o /usr/local/bin/drush "https://github.com/drush-ops/drush-
launcher/releases/download/$DRUSH_VERSION/drush.phar" && \  
chmod +x /usr/local/bin/drush  
  
#drupal command  
RUN curl https://drupalconsole.com/installer -L -o drupal.phar && \  
mv drupal.phar /usr/local/bin/drupal && \  
chmod +x /usr/local/bin/drupal

