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
php5.6-cli \  
php5.6-common \  
php5.6-bcmath \  
php5.6-bz2 \  
php5.6-curl \  
php5.6-gd \  
php5.6-intl \  
php5.6-json \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-mysql \  
php5.6-opcache \  
php5.6-xml \  
php5.6-xsl \  
php5.6-zip \  
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
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
  
## Update npm  
RUN npm -g update npm  
## Instal global node packages  
RUN npm install -g gulp bower  

