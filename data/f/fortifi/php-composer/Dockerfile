FROM debian:stretch  
  
ENV TERM linux  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install \  
wget \  
git \  
unzip \  
php7.0-cli \  
php7.0-apcu \  
php7.0-bcmath \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-geoip \  
php7.0-gmp \  
php7.0-imagick \  
php7.0-intl \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-redis \  
php7.0-soap \  
php7.0-xml \  
php7.0-xsl \  
php7.0-dev \  
php7.0-zip \  
php-memcached \  
php-mailparse \  
&& \  
apt-get -y clean  
  
RUN git clone https://github.com/hnw/php-timecop && \  
cd php-timecop && \  
phpize && \  
./configure && \  
make && \  
make install  
  
RUN echo "extension=timecop.so" >/etc/php/7.0/cli/conf.d/20-timecop.ini  
  
# Force build to fail if the modules can't be loaded  
RUN php -m | grep timecop >/dev/null  
  
RUN wget https://getcomposer.org/composer.phar && \  
chmod 0755 composer.phar && \  
mv composer.phar /usr/local/bin && \  
ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  

