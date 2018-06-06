FROM comicrelief/php-base:7.1  
RUN a2ensite symfony ; apt-get update \  
; apt-get install -y --fix-missing libxml2-dev mysql-client \  
libpng12-dev libjpeg62-turbo-dev libfreetype6-dev imagemagick libmagick++-dev  
  
# PHP extensions for Drupal  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
; docker-php-ext-install gd soap \  
; pecl install imagick ; docker-php-ext-enable imagick  
  
#Platform.sh  
RUN curl -sS https://platform.sh/cli/installer | php  
RUN export PATH="/root/.platformsh/bin:$PATH"  
  
# Install phing & drush  
RUN composer global config bin-dir /usr/local/bin \  
; composer global require drush/drush  
  
# FE tool  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
; apt-get install -y nodejs ruby ruby-dev ; npm install -g grunt-cli \  
; gem install bundler compass ; bundle config --global jobs 8  

