FROM php:5-apache  
  
RUN apt-get update && apt-get install -y \  
git \  
subversion \  
wget \  
libxml2-dev \  
ssmtp \  
libbz2-dev \  
libpng-dev \  
libc-client-dev \  
libkrb5-dev \  
libicu-dev \  
libmcrypt-dev \  
libpspell-dev \  
librecode-dev \  
libtidy-dev \  
libxslt-dev \  
libmagickwand-dev \  
libapache2-mod-geoip \  
libapache2-mod-security2 \  
ssl-cert  
  
RUN docker-php-ext-configure \  
imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install \  
bcmath \  
bz2 \  
calendar \  
exif \  
gd \  
gettext \  
imap \  
intl \  
mcrypt \  
mysql \  
mysqli \  
pdo_mysql \  
pspell \  
recode \  
shmop \  
soap \  
sysvsem \  
sysvshm \  
tidy \  
wddx \  
xsl \  
zip \  
&& pecl install \  
gender \  
imagick \  
mongodb \  
&& docker-php-ext-enable \  
gender \  
imagick \  
mongodb  
  
RUN cd /etc/apache2/mods-enabled \  
&& a2ensite default-ssl \  
&& a2enmod actions \  
&& a2enmod auth_digest \  
&& a2enmod authz_groupfile \  
&& a2enmod cgi \  
&& a2enmod expires \  
&& a2enmod geoip \  
&& a2enmod headers \  
&& a2enmod include \  
&& a2enmod proxy \  
&& a2enmod proxy_http \  
&& a2enmod rewrite \  
&& a2enmod security2 \  
&& a2enmod speling \  
&& a2enmod ssl \  
&& a2enmod suexec \  
&& a2enmod unique_id \  
&& service apache2 restart  
  
RUN echo "mailhub=mailcatcher:1025\nUseTLS=NO\nFromLineOverride=YES" >
/etc/ssmtp/ssmtp.conf  
  
RUN curl https://getcomposer.org/download/$(curl -LSs
https://api.github.com/repos/composer/composer/releases/latest | grep
'tag_name' | sed -e 's/.*: "//;s/".*//')/composer.phar > composer.phar \  
&& chmod +x composer.phar \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN curl https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar > wp-cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
RUN echo "mailhub=mailcatcher:1025\nUseTLS=NO\nFromLineOverride=YES" >
/etc/ssmtp/ssmtp.conf  
  
RUN apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
COPY php.ini /usr/local/etc/php/  
  
WORKDIR /var/www/html  

