FROM anezi/debian-dev-tools  
  
LABEL maintainer Hassan Amouhzi  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install php  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg && \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list && \  
apt-get update && apt-get install -y \  
php7.1-cli \  
php7.1-curl \  
php7.1-intl \  
php7.1-mcrypt \  
php7.1-memcached \  
php7.1-imagick \  
php7.1-mysql \  
php7.1-apcu \  
php7.1-xml \  
php7.1-zip \  
php7.1-mbstring \  
php7.1-fpm \  
&& rm -rf /var/lib/apt/lists/*  
# Intall composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN service php7.1-fpm start

