FROM gaxze/php-base:7.1.x  
  
# Drupal Console commands  
RUN curl -L https://github.com/hechoendrupal/drupal-console-
launcher/releases/download/1.0.2/drupal.phar > drupal \  
&& chmod +x drupal \  
&& mv drupal /usr/local/bin/  
  
# Install drush  
RUN composer global config bin-dir /usr/local/bin \  
; composer global require drush/drush  
  
# FE  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
; apt-get install -y nodejs ; npm install -g grunt-cli ; npm install -g yarn  

