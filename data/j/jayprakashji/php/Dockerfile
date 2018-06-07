FROM php:7.1-apache  
  
RUN apt-get update \  
# gd  
&& apt-get install -y --no-install-recommends libfreetype6-dev
libjpeg62-turbo-dev libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
# iconv  
&& docker-php-ext-install -j$(nproc) iconv \  
# mcrypt  
&& apt-get install -y --no-install-recommends libmcrypt-dev \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
# intl  
&& apt-get install -y --no-install-recommends libicu-dev \  
&& docker-php-ext-install intl \  
# mysql  
&& docker-php-ext-install mysqli pdo_mysql \  
# composer  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer \  
# mbstring  
&& docker-php-ext-install mbstring \  
# soap  
&& apt-get install -y --no-install-recommends libxml2-dev \  
&& docker-php-ext-install soap \  
# opcache  
&& docker-php-ext-install opcache \  
# zip  
&& docker-php-ext-install zip \  
# git  
&& apt-get install -y --no-install-recommends git \  
# xsl  
&& apt-get install -y --no-install-recommends libxslt-dev \  
&& docker-php-ext-install xsl \  
# bcmath  
&& docker-php-ext-install bcmath \  
# ldap  
&& apt-get install -y --no-install-recommends libldap2-dev \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install ldap \  
# redis  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
# memcached  
&& apt-get install -y libmemcached-dev zlib1g-dev \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached \  
\  
# Enable Apache mod_rewrite  
&& a2enmod rewrite \  
# cleanup  
&& rm -rf /var/lib/apt/lists/*  
  
# Install ssmtp Mail Transfer Agent  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ssmtp \  
&& apt-get clean \  
&& echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf \  
&& echo 'sendmail_path = "/usr/sbin/ssmtp -t"' >
/usr/local/etc/php/conf.d/mail.ini \  
# cleanup  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Default date.timezone  
ENV PHP_TIMEZONE Europe/Bratislava  
# Default DocumentRoot  
ENV APACHE_DOC_ROOT /var/www/html  
# Modified php.ini  
COPY ./999-php.ini /usr/local/etc/php/conf.d/  
  
  
ENV XDEBUG_ENABLE 1  
RUN pecl config-set preferred_state beta \  
&& pecl install -o -f xdebug \  
&& rm -rf /tmp/pear \  
&& pecl config-set preferred_state stable \  
&& docker-php-ext-enable xdebug  
  
COPY ./99-xdebug.ini /usr/local/etc/php/conf.d/  
  
  
  
  
  
  
  
# For debug  
# Debug tools  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
mysql-client \  
less \  
vim \  
git \  
mc \  
openssh-client \  
nmap \  
&& rm -rf /var/lib/apt/lists/*  
COPY ./index.php /var/www/html/index.php  
  
  
  
  
  
# Start!  
COPY ./entrypoint.sh /usr/local/bin/  
CMD ["entrypoint.sh"]  
  
  
  
  
  
  
  

