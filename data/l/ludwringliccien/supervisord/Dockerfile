FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Add repository PPA php 7.1  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y build-essential make  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y language-pack-en-base &&\  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository
ppa:ondrej/php  
  
# Update the package repository and Install base packages  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes nano wget curl git vim supervisor unzip  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install -y php7.1 \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-dba \  
php7.1-dev \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-opcache \  
php7.1-soap \  
php7.1-xml \  
php7.1-json \  
php7.1-zip \  
php-redis  
  
# Install oci8 without internet  
RUN wget "https://s3.amazonaws.com/simonetti-tests/oci8/instantclient-sdk-
linux.x64-12.1.0.2.0.zip" -P /tmp/ && \  
wget "https://s3.amazonaws.com/simonetti-tests/oci8/instantclient-basic-
linux.x64-12.1.0.2.0.zip" -P /tmp/  
  
# Unzip them  
RUN unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/ &&
\  
unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/  
  
# Install oci8  
RUN ln -s /usr/local/instantclient_12_1 /usr/local/instantclient && \  
ln -s /usr/local/instantclient/libclntsh.so.12.1
/usr/local/instantclient/libclntsh.so && \  
echo 'instantclient,/usr/local/instantclient' | pecl install oci8  
  
# Install libaio1 package needed for connecting to Oracle  
RUN apt-get update && apt-get install -y libaio1 sudo  
  
# Cleaning  
RUN apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
# Confugure cli php.ini  
RUN sed -i '$a extension=oci8.so' /etc/php/7.1/cli/php.ini  
  
# Nginx oci8 ini  
ADD oci8.ini /etc/php/versionPHP/mods-available/  
  
# Add workers  
ADD mailers-worker.conf /etc/supervisor/conf.d/  
ADD packages-worker.conf /etc/supervisor/conf.d/  
ADD reports-worker.conf /etc/supervisor/conf.d/  
ADD tracker-worker.conf /etc/supervisor/conf.d/  
  
# Set user deployer  
RUN useradd -g 33 -m deployer && echo "deployer:deployer" | chpasswd &&
adduser deployer sudo  
RUN echo "deployer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
USER deployer  
  
WORKDIR /home/deployer  
  
CMD sudo supervisord -n

