#++++++++++++++++++++++++++++++++++++++  
# Ubuntu 14.04 PHP Docker container  
#++++++++++++++++++++++++++++++++++++++  
  
FROM ubuntu:14.04  
MAINTAINER mblaschke82@gmail.com  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Install apt-add-repository  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  
  
# Install ansible  
RUN set -x \  
&& apt-add-repository ppa:ansible/ansible \  
&& apt-get update \  
&& apt-get install -y \  
ansible \  
python-apt \  
aptitude \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  
  
# Install tools  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
lsb-release \  
sudo \  
zip \  
unzip \  
bzip2 \  
imagemagick \  
graphicsmagick \  
wget \  
curl \  
net-tools \  
moreutils \  
dnsutils \  
mysql-client \  
openssh-client \  
rsync \  
git \  
cron \  
anacron \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  
  
# Install services  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
ssmtp \  
dnsmasq \  
supervisor \  
openssh-server \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  
  
# Install php  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
php5-cli \  
php5-fpm \  
php5-json \  
php5-intl \  
php5-curl \  
php5-mysqlnd \  
php5-xdebug \  
php5-memcached \  
php5-mcrypt \  
php5-gd \  
php5-sqlite \  
php5-xmlrpc \  
php5-xsl \  
php5-geoip \  
php5-ldap \  
php5-memcache \  
php5-memcached \  
php5-imagick \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  
  
# Update  
RUN set -x \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  

