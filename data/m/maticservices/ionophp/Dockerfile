FROM php:5.6-apache  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common gnupg \  
&& curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32 \  
&& add-apt-repository "deb http://mirrors.kernel.org/ubuntu artful main
universe" \  
&& apt-get update \  
&& apt-get install -y \  
libmcrypt-dev libpng-dev \  
build-essential libz-dev \  
librabbitmq4 librabbitmq-dev \  
libicu-dev \  
mysql-client \  
openssl \  
wget \  
git \  
unzip \  
cron \  
vim \  
supervisor \  
curl \  
librtmp1 \  
google-chrome-stable \  
&& CFLAGS="-fgnu89-inline" docker-php-ext-enable opcache \  
# amqp  
&& pecl install amqp \  
&& docker-php-ext-enable amqp \  
# xdebug  
&& pecl install xdebug-2.5.5 \  
&& docker-php-ext-enable xdebug \  
# timecop  
&& curl -L https://github.com/hnw/php-timecop/archive/master.tar.gz | tar -xz
\  
&& cd php-timecop-master && phpize && ./configure && make && make install \  
&& docker-php-ext-enable timecop \  
# ioncube  
&& curl -L
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
| tar -xz \  
&& cp ioncube/ioncube_loader_lin_5.6.so $(php-config --extension-dir) \  
&& echo "zend_extension = $(php-config --extension-
dir)/ioncube_loader_lin_5.6.so" > $PHP_INI_DIR/conf.d/00_docker-php-ext-
ioncube_loader_lin_5.6.ini \  
&& rm -r ioncube \  
# composer  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer \  
# cleanup  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get remove -y build-essential libz-dev \  
&& apt-get autoremove -y \  
&& rm -rf /tmp/pear  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install nodejs  
  
RUN docker-php-ext-install \  
pdo \  
pcntl \  
pdo_mysql \  
mcrypt \  
zip \  
gd \  
bcmath \  
intl  
  
RUN npm install -g @angular/cli  
  
COPY php.ini /usr/local/etc/php/php.ini  
COPY default.conf /etc/apache2/sites-enabled/000-default.conf  
COPY supervisord/supervisord.conf /etc/supervisor/supervisord.conf  
COPY iv_cron /etc/cron.d/iv_cron  
  
RUN chmod 0644 /etc/cron.d/iv_cron  
RUN touch /var/log/cron.log  
RUN ln -s /app /var/www/site  
RUN a2enmod headers rewrite  
  
RUN printenv >> /etc/environment  

