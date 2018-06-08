FROM php:7.0-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install npm  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
gnupg2  
  
RUN printf "deb https://deb.nodesource.com/node_8.x jessie main\ndeb-src
https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list  
  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
-  
  
ADD bin/docker-php-pecl-install /usr/local/bin/  
  
RUN apt-get update && apt-get install -y \  
git \  
imagemagick \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libjpeg-turbo-progs \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
mysql-client \  
pngquant \  
python \  
ssmtp \  
sudo \  
unzip \  
wget \  
zlib1g-dev \  
nodejs \  
vim \  
&& docker-php-ext-install \  
bcmath \  
curl \  
exif \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pcntl \  
pdo_mysql \  
soap \  
zip \  
&& apt-get clean && apt-get autoremove -q \  
&& rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/* \  
&& a2enmod deflate expires headers mime rewrite \  
&& a2dissite 000-default \  
&& echo "<Directory /var/www/html>\nAllowOverride All\n</Directory>" >
/etc/apache2/conf-enabled/allowoverride.conf \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& echo "sendmail_path = /usr/sbin/ssmtp -t" > /usr/local/etc/php/conf.d/conf-
sendmail.ini \  
&& echo "date.timezone='Europe/Paris'\n" > /usr/local/etc/php/conf.d/conf-
date.ini  
  
# Install Gulp  
RUN npm install --global gulp-cli  
  
# Install Uploadprogress  
RUN git clone https://git.php.net/repository/pecl/php/uploadprogress.git \  
&& cd uploadprogress \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& cd .. \  
&& rm -rf uploadprogress \  
&& echo "extension=uploadprogress.so" > /usr/local/etc/php/conf.d/conf-
uploadprogress.ini  
  
# Install PhpRedis.  
RUN git clone https://github.com/phpredis/phpredis.git \  
&& cd phpredis \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& cd .. \  
&& rm -rf phpredis \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/conf-redis.ini  
  
# Install Composer.  
RUN cd /usr/local \  
&& curl -sS https://getcomposer.org/installer | php \  
&& chmod +x /usr/local/composer.phar \  
&& ln -s /usr/local/composer.phar /usr/local/bin/composer \  
&& echo 'PATH="$HOME/.composer/vendor/bin:$PATH"' >> $HOME/.bashrc  
  
# Install Drush.  
RUN composer global require drush/drush:@stable  
  
RUN docker-php-pecl-install \  
xdebug  
  
# Install Coder.  
# Install Coder and configure Code sniffer.  
RUN composer global require drupal/coder:8.2.* \  
&& composer global require dealerdirect/phpcodesniffer-composer-installer \  
&& composer clear-cache \  
&& echo 'alias drupalcs="phpcs --standard=Drupal
--extensions='php,module,inc,install,test,profile,theme,css,info,txt,md'"' >>
$HOME/.bashrc \  
&& echo 'alias drupalcsp="phpcs --standard=DrupalPractice
--extensions='php,module,inc,install,test,profile,theme,css,info,txt,md'"' >>
$HOME/.bashrc \  
&& echo 'alias drupalcbf="phpcbf --standard=Drupal
--extensions='php,module,inc,install,test,profile,theme,css,info,txt,md'"' >>
$HOME/.bashrc  
  
# Install Drupal console.  
RUN curl https://drupalconsole.com/installer -L -o /usr/local/bin/drupal \  
&& chmod +x /usr/local/bin/drupal \  
&& drupal init  
  
# Add some bash aliases.  
RUN echo 'alias ll="ls -l"' >> $HOME/.bashrc \  
&& echo 'alias lll="ls -al"' >> $HOME/.bashrc  
  
WORKDIR /project/web  
  
# Xdebug conf.  
COPY xdebug.ini /usr/local/etc/php/conf.d/conf-xdebug.ini  

