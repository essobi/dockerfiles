#  
#--------------------------------------------------------------------------  
# Image Setup  
#--------------------------------------------------------------------------  
#  
FROM phusion/baseimage:latest  
  
MAINTAINER Ilya Shtrikul <shtricul@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
# Add the "PHP 7" ppa  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Install "PHP Extentions", "libraries", "Software's"  
RUN apt-get update && \  
apt-get install -y --force-yes \  
zsh \  
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
php7.0-xdebug \  
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
nano \  
postgresql-client  
  
#####################################  
# Composer:  
#####################################  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
  
#####################################  
# Non-Root User:  
#####################################  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ARG PUID=1000  
ARG PGID=1000  
ARG CONTAINER=container  
ENV CONTAINER ${CONTAINER}  
RUN groupadd -g $PGID ${CONTAINER} && \  
useradd -u $PUID -g ${CONTAINER} -m ${CONTAINER}  
  
#####################################  
# Set Timezone  
#####################################  
ARG TZ=UTC  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
#####################################  
# Crontab  
#####################################  
USER root  
  
COPY ./crontab /var/spool/cron/crontabs  
  
#####################################  
# ssh:  
#####################################  
ADD ./ssh/insecure_id_rsa /tmp/id_rsa  
ADD ./ssh/insecure_id_rsa.pub /tmp/id_rsa.pub  
  
RUN rm -f /etc/service/sshd/down && \  
cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys \  
&& cat /tmp/id_rsa.pub >> /root/.ssh/id_rsa.pub \  
&& cat /tmp/id_rsa >> /root/.ssh/id_rsa \  
&& rm -f /tmp/id_rsa* \  
&& chmod 644 /root/.ssh/authorized_keys /root/.ssh/id_rsa.pub \  
&& chmod 400 /root/.ssh/id_rsa  
  
#####################################  
# Node / NVM:  
#####################################  
USER ${CONTAINER}  
# Check if NVM needs to be installed  
ARG NODE_VERSION=stable  
ENV NODE_VERSION ${NODE_VERSION}  
ENV NVM_DIR /home/${CONTAINER}/.nvm  
# Install nvm (A Node Version Manager)  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash &&
\  
. $NVM_DIR/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias ${NODE_VERSION} && \  
npm install -g gulp bower vue-cli  
  
# Wouldn't execute when added to the RUN statement in the above block  
# Source NVM when loading bash since ~/.profile isn't loaded on non-login
shell  
RUN echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc  
  
# Add NVM binaries to root's .bashrc  
USER root  
RUN echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="/home/${CONTAINER}/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
# Clean up  
USER root  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set default work directory  
WORKDIR /var/www

