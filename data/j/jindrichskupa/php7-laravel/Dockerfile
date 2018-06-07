FROM debian:jessie-slim  
  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
RUN \  
apt-get update && \  
apt-get install -y \  
wget gnupg  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
wget -O- http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
RUN \  
apt-get update && \  
apt-get install -y \  
curl \  
unzip \  
vim \  
git \  
apt-transport-https \  
locales \  
iptables \  
apache2 \  
php7.0 \  
php7.0-mysql \  
php7.0-mysql \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-gd \  
php7.0-memcache \  
php7.0-zip \  
php7.0-curl \  
php-pear \  
php7.0-apcu \  
php7.0-cli \  
php7.0-curl \  
php7.0-mcrypt \  
php7.0-sqlite \  
php7.0-intl \  
php7.0-tidy \  
php7.0-imap \  
php7.0-json \  
php7.0-imagick \  
php7.0-common \  
libapache2-mod-php7.0 \  
libapache2-mod-rpaf && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2enmod alias && \  
a2enmod dir && \  
a2enmod env && \  
a2enmod mime && \  
a2enmod reqtimeout && \  
a2enmod rewrite && \  
a2enmod status && \  
a2enmod filter && \  
a2enmod deflate && \  
a2enmod setenvif && \  
a2enmod vhost_alias && \  
a2enmod ssl && \  
a2enmod php7.0 && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require 'laravel/installer' && \  
echo 'export PATH=$PATH:$HOME/.composer/vendor/bin' >> $HOME/.bash_profil && \  
sed -i '/DocumentRoot/s/html/html\/public/' /etc/apache2/sites-
enabled/000-default.conf && \  
curl -LO https://deployer.org/deployer.phar && mv deployer.phar
/usr/local/bin/dep && \  
chmod +x /usr/local/bin/dep  
  
RUN wget http://deb.nodesource.com/gpgkey/nodesource.gpg.key -O- | apt-key add
- && \  
echo 'deb https://deb.nodesource.com/node_6.x jessie main' >
/etc/apt/sources.list.d/nodejs.list && \  
apt-get update && apt-get -y install nodejs && apt-get autoremove -y && apt-
get clean && \  
rm -rf /var/lib/apt/lists  
  
RUN echo Europe/Brussels > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata && \  
echo 'en_US.UTF-8 UTF-8\n\  
cs_CZ.UTF-8 UTF-8\n' \  
>> /etc/locale.gen && \  
/usr/sbin/locale-gen  
  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY ./run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
EXPOSE 80  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

