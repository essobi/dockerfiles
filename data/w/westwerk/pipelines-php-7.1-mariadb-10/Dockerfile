FROM westwerk/base-ubuntu  
MAINTAINER Michael Ruettgers <mr@westwerk.ac>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Define packages to be installed  
ENV PACKAGES \  
make \  
git \  
curl \  
phpunit \  
mariadb-server-10.0 \  
php7.1-cli \  
php7.1-common \  
php7.1-bcmath \  
php7.1-bz2 \  
php7.1-curl \  
php7.1-gd \  
php7.1-intl \  
php7.1-json \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-opcache \  
php7.1-xml \  
php7.1-xsl \  
php7.1-zip \  
libxrender1 \  
libfontconfig1  
  
# Install packages && cleanup  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install $PACKAGES && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y  
  
# Disable warnings for unknown host keys  
RUN ( [ -d /etc/ssh/ ] || mkdir -p /etc/ssh ) && \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
# Setup build tools  
## Install composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
## Install node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
## Update npm  
RUN npm -g update npm@v4.5.0  
## Instal global node packages  
RUN npm install -g gulp bower yarn  

