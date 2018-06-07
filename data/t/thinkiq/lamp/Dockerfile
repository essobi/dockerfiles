FROM ubuntu:16.04  
MAINTAINER Bruce McCleave<bruce@thinkiq.com>  
  
USER root  
COPY config/docker-startup.sh /usr/local/bin/docker-startup.sh  
RUN chmod 755 /usr/local/bin/docker-startup.sh && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install software-properties-common && \  
apt-get update && \  
apt-get -y install debconf-utils && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y sudo \  
curl \  
tar \  
git \  
nano \  
memcached \  
mysql-client \  
openssh-server \  
openssh-client \  
openssl \  
rsync \  
apache2 \  
vim \  
bash-completion \  
unzip \  
php \  
wget \  
tzdata \  
php-cli \  
php-phar \  
php-zip \  
php-bz2 \  
php-ctype \  
php-mysqli \  
php-mysql \  
php-pdo \  
php-json \  
php-curl \  
php-gd \  
php-gmp \  
php-mcrypt \  
php-dom \  
php-xml \  
php-iconv \  
libapache2-mod-php \  
php-dev \  
php-gd \  
php-memcache \  
php-pspell \  
php-snmp \  
php-memcached \  
snmp \  
php-xmlrpc \  
php7.0-zip \  
libapache2-modsecurity \  
sendmail \  
php-mbstring \  
php7.0-mbstring \  
php-gettext \  
supervisor && \  
echo "#disable ipv6" | sudo tee -a /etc/sysctl.conf && \  
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf && \  
echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
&& \  
echo "net.ipv6.conf.lo.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf && \  
sysctl -p && \  
groupadd -r thinkiq && sudo useradd thinkiq -s /bin/bash -g sudo -m && \  
echo "root ALL=(ALL) ALL" > /etc/sudoers && \  
echo "thinkiq ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
echo "Defaults env_reset" >>/etc/sudoers && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
COPY config/apache2.conf /etc/apache2/apache2.conf  
USER thinkiq  
WORKDIR /home/thinkiq  
  
# The root password will need to be set after starting the continar to allow
for logins  
  
EXPOSE 80 443  
VOLUME ["/var/www/html"]

