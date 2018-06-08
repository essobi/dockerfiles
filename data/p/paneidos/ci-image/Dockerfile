FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get -y \--no-install-recommends install wget git apt-transport-https lsb-
release ca-certificates && \  
wget -O - https://packages.sury.org/php/apt.gpg | apt-key add \- && \  
wget -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
wget -O - https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- && \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >>
/etc/apt/sources.list.d/php.list && \  
echo "deb https://deb.nodesource.com/node_8.x $(lsb_release -sc) main" >>
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb-src https://deb.nodesource.com/node_8.x $(lsb_release -sc) main" >>
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y \--no-install-recommends php7.2-bcmath php7.2-cli
php7.2-curl php7.2-gd \  
php7.2-mysql php7.2-soap php7.2-xml php7.2-xsl php7.2-zip php7.2-mbstring
php7.2-xdebug curl openssh-client \  
nodejs yarn mariadb-client build-essential && apt-get clean && \  
curl --silent \--show-error https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer && \  
useradd -m -d /home/ci -U -u 1000 ci  
  
USER ci  
  
RUN composer global require "laravel/envoy=~1.0"  

