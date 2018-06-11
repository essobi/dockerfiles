FROM phusion/baseimage:latest  
  
MAINTAINER ChaoYi Lu <iyoahcul@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
RUN apt-get update && \  
apt-get install -y --force-yes \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-json \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite \  
php7.0-sqlite3 \  
php7.0-zip \  
php7.0-memcached \  
php7.0-gd \  
pkg-config \  
php-dev \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
libsqlite3-dev \  
sqlite3 \  
git \  
curl \  
vim \  
postgresql-client \  
&& apt-get clean  
  
#####################################  
# Composer:  
#####################################  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/xijinfa/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
  
RUN . ~/.bashrc  
  
#####################################  
# Non-Root User:  
#####################################  
ARG PUID=1000  
ARG PGID=1000  
RUN groupadd -g $PGID dev && \  
useradd -u $PUID -g dev -m dev  
  
USER dev  
  
#####################################  
# Node / NVM:  
#####################################  
ARG NODE_VERSION=stable  
ENV NODE_VERSION stable  
ARG INSTALL_NODE=true  
ENV INSTALL_NODE true  
ENV NVM_DIR /home/dev/.nvm  
RUN if [ ${INSTALL_NODE} = true ]; then \  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh |
bash && \  
. ~/.nvm/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias ${NODE_VERSION} && \  
npm install -g gulp bower vue-cli \  
;fi  
  
RUN if [ ${INSTALL_NODE} = true ]; then \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc \  
;fi  
  

