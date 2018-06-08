FROM debian:stretch  
  
ENV TERM linux  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
openssh-client \  
procps  
  
RUN curl -SLo /etc/apt/trusted.gpg.d/sury-php.gpg
https://packages.sury.org/php/apt.gpg && \  
echo "deb https://packages.sury.org/php/ stretch main" >
/etc/apt/sources.list.d/php.list  
  
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
php7.1-redis \  
php7.1-sqlite3 \  
php7.1-xml \  
php7.1-zip  
  
# slim down image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man/?? /usr/share/man/??_*  
  
# Install Composer globally  
RUN curl -S https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Global configurations  
RUN echo "America/Sao_Paulo" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# setup workdir  
RUN mkdir -p /var/www/mercadoinca  
  
WORKDIR /var/www/mercadoinca  

