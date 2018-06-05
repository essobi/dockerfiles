FROM drupal:7.54-apache  
MAINTAINER olof olsson <olof.olsson@snd.gu.se>  
  
RUN apt-get update &&\  
apt-get install -y mysql-client &&\  
apt-get install -y git  
  
RUN echo "short_open_tag = Off" > /usr/local/etc/php/conf.d/short_tags_off.ini  
  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_VERSION 1.1.2  
# Install Composer and drush  
ENV COMPOSER_INSTALLER_SHA384
"55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30"  
RUN php -r "readfile('https://getcomposer.org/installer');" > /tmp/composer-
setup.php &&\  
php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !==
'${COMPOSER_INSTALLER_SHA384}') { unlink('/tmp/composer-setup.php'); echo
'Invalid installer' . PHP_EOL; exit(1); }" &&\  
export PATH="$HOME/.composer/vendor/bin:$PATH" &&\  
php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php &&\  
composer --version &&\  
composer global require drush/drush:8.* &&\  
composer global require "squizlabs/php_codesniffer=*" &&\  
composer global require drupal/coder &&\  
phpcs --config-set installed_paths /composer/vendor/drupal/coder/coder_sniffer
&&\  
phpcs --config-set default_standard Drupal &&\  
drush @none dl registry_rebuild-7.x &&\  
drush cc drush  
  
RUN echo 'alias init-site="drush updb -y && drush rr && drush composer-json-
rebuild && drush composer-manager install -y"' >> ~/.bashrc  
  
WORKDIR /var/www/html/sites/default  
  
VOLUME ["/src"]

