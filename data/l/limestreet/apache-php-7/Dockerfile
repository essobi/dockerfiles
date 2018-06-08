FROM php:7-apache  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli pdo pdo_mysql opcache zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# Install git  
RUN apt-get update && apt-get install -y git  
  
# Install mysql-client  
RUN apt-get update && apt-get install -y mysql-client  
  
# Install unzip  
#RUN apt-get update && apt-get install -y unzip  
# Adjusting php settings  
RUN touch /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "upload_max_filesize = 32M;" >> /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "post_max_size = 32M;" >> /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "memory_limit = 512M;" >> /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "date.timezone = \"Europe/Warsaw\";" >>
/usr/local/etc/php/conf.d/patryk.ini \  
&& php -v && php -i  
  
# Install WP-CLI, Composer, wp tgmpa-plugin and PHPUnit  
RUN curl -L https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar -o wp-cli.phar \  
&& chmod +x wp-cli.phar && mv wp-cli.phar /usr/bin/wp \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php \  
&& mv composer.phar /usr/local/bin/composer && rm -rf composer-setup.php \  
&& curl -L https://github.com/itspriddle/wp-cli-tgmpa-
plugin/archive/v0.3.0.zip -o wp-cli-tgmpa-plugin.zip \  
&& wp package install wp-cli-tgmpa-plugin.zip --allow-root \  
&& curl -L https://phar.phpunit.de/phpunit-5.7.phar -o phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit  
  
# Install Node and npm packages  
RUN apt-get update && apt-get -y install gnupg2 \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get -y install nodejs && rm -rf /var/lib/apt/lists/*  
  
#RUN apt-get update && apt-get install -y bzip2  
# PhantomJS  
#RUN export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" \  
# && curl -L
https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 -o
$PHANTOM_JS.tar.bz2 \  
# && tar xvjf $PHANTOM_JS.tar.bz2 \  
# && mv $PHANTOM_JS /usr/local/share \  
# && rm -f $PHANTOM_JS.tar.bz2 \  
# && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \  
# && npm install -g phantomjs \  
# && npm install -g grunt-cli \  
# && npm install -g jshint \  
# && npm install -g pa11y  
# && npm install -g casperjs  
RUN npm install -g grunt-cli \  
&& npm install -g phantomjs \  
&& npm install -g pa11y  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www  

