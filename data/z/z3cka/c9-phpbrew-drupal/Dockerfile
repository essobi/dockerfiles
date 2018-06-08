# c9+php+drupal  
FROM z3cka/c9-php  
MAINTAINER Casey Grzecka <c@sey.gr>  
  
ARG phpVersion="php-5.6.26"  
ENV PHPBREW_PHP $phpVersion  
  
RUN phpbrew install $phpVersion +default +apxs2 +curl +mysql  
RUN phpbrew switch $phpVersion  
RUN phpbrew ext install gd  
  
RUN ln -s /etc/php5/cli/conf.d/30-xdebug.ini
/root/.phpbrew/php/$phpVersion/var/db/xdebug.ini  
  
RUN composer global require drush/drush:7.*  
  
RUN mkdir ~/drush8 && \  
cd ~/drush8 && \  
composer require "drush/drush:8.*"  
RUN mkdir ~/drush7 && \  
cd ~/drush7 && \  
composer require "drush/drush:7.*"  
RUN mkdir ~/drush6 && \  
cd ~/drush7 && \  
composer require "drush/drush:6.*"  
  
RUN ln -s /root/drush6/vendor/bin/drush /usr/local/bin/drush6 && \  
ln -s /root/drush7/vendor/bin/drush /usr/local/bin/drush && \  
ln -s /root/drush7/vendor/bin/drush /usr/local/bin/drush7 && \  
ln -s /root/drush8/vendor/bin/drush /usr/local/bin/drush8  
  
# Add mysql-client as a nice to have  
RUN apt update && apt install -y mysql-client  

