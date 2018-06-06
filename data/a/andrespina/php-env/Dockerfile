FROM php:7.1.11-fpm  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libpcre3-dev \  
curl \  
mysql-client \  
git-core \  
build-essential  
  
RUN docker-php-ext-install -j$(nproc) mysqli && \  
docker-php-ext-install -j$(nproc) pdo_mysql && \  
docker-php-ext-install -j$(nproc) iconv mcrypt && \  
docker-php-ext-install -j$(nproc) zip && \  
docker-php-ext-configure opcache --enable-opcache && \  
docker-php-ext-install -j$(nproc) opcache && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set the Drush version.  
ENV DRUSH_VERSION 8.1.15  
RUN curl -fsSL -o /usr/local/bin/drush "https://github.com/drush-
ops/drush/releases/download/$DRUSH_VERSION/drush.phar" && \  
chmod +x /usr/local/bin/drush  
  
# Set composer and php sniffer.  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer
&& \  
php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=1.5.5 && \  
composer self-update  
  
RUN rm -rf /tmp/*  
ENV PATH=$PATH:/root/.composer/vendor/bin/  
  
RUN composer global require squizlabs/php_codesniffer:2.9.1  
RUN composer global require drupal/coder:dev-8.x-2.x  
  
RUN phpcs --config-set installed_paths
/root/.composer/vendor/drupal/coder/coder_sniffer  
  
RUN ln -s
/composer/vendor/drupal/coder/coder_sniffer/Drupal/composer/vendor/squizlabs/php_codesniffer/CodeSniffer/Standards/Drupal  
RUN ln -s
/composer/vendor/drupal/coder/coder_sniffer/DrupalPractice/composer/vendor/squizlabs/php_codesniffer/CodeSniffer/Standards/Drupal/Practice  
  
# install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g eslint --silent && \  
npm install -g eslint-plugin-import --silent && \  
npm install -g eslint-plugin-jsx-a11y --silent && \  
npm install -g eslint-config-airbnb --silent && \  
npm install -g eslint-plugin-react --silent  
  
# Install gulp.  
RUN npm install -g gulp-cli gulp --silent  

