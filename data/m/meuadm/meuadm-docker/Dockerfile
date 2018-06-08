FROM debian:jessie  
  
# Needed for edit files inside container and  
# to suppress messages like "debconf: unable to initialize frontend: Dialog"  
ENV TERM linux  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
lsb-release \  
nano \  
wget \  
vim  
  
RUN wget -O /etc/apt/trusted.gpg.d/sury-php.gpg
https://packages.sury.org/php/apt.gpg && \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/sury-php.list  
  
RUN apt-get update && apt-get install -y \  
php7.1 \  
php7.1-bcmath \  
php7.1-cli \  
php7.1-curl \  
php7.1-intl \  
php7.1-json \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-opcache \  
php7.1-sqlite3 \  
php7.1-xml \  
php7.1-zip  
  
# Install Composer globally  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install PHPUnit globally  
RUN curl -sSLo /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar &&
chmod +x /usr/local/bin/phpunit  
  
# Global configurations  
RUN echo "America/Sao_Paulo" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# slim down image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man/?? /usr/share/man/??_*  
  
# setup workdir  
RUN mkdir -p /var/www/meuadm  
  
WORKDIR /var/www/meuadm

