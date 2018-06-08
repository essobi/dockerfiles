FROM debian:jessie  
  
################################################################################  
# Installation de wget  
################################################################################  
  
RUN \  
apt-get -qq update --fix-missing && \  
apt-get -qq install -y \  
wget  
  
################################################################################  
# Mise en place de DotDeb  
################################################################################  
  
RUN \  
echo "deb http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
wget http://www.dotdeb.org/dotdeb.gpg -O dotdeb.gpg && \  
apt-key add dotdeb.gpg  
  
################################################################################  
# Installation des Libs Apache / PHP7 / Extensions de PHP  
################################################################################  
  
RUN \  
apt-get -qq update --fix-missing && \  
apt-get -qq install -y \  
php7.0 \  
apache2 \  
libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-gd \  
php7.0-imagick \  
php7.0-dev \  
php7.0-curl \  
php7.0-opcache \  
php7.0-cli \  
php7.0-intl \  
php7.0-json \  
php7.0-mcrypt \  
php7.0-common \  
php7.0-apcu-bc \  
php7.0-mbstring \  
php7.0-zip \  
php7.0-xml  
  
################################################################################  
# Installation de phpcsfixer  
################################################################################  
  
RUN \  
wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer && \  
chmod a+x php-cs-fixer && \  
mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
################################################################################  
# Suppression des fichiers temporaires.  
################################################################################  
  
  
RUN \  
apt-get -qq clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

