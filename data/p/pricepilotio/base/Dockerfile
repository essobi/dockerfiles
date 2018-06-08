################################################################################  
# #  
# {o,o} #  
# |)__) #  
# -"-"\- #  
# #  
################################################################################  
#  
# Apache docker image  
#  
##################################---BASE---####################################  
  
FROM ubuntu:16.04  
  
################################################################################  
  
################################---MAINTAINER---################################  
  
MAINTAINER Price pilot <hello@pricepilot.io>  
  
################################################################################  
  
#################################---ENV---######################################  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL=C.UTF-8  
  
################################################################################  
  
###################################---BUILD---##################################  
  
RUN apt-get update && apt-get -y upgrade; \  
apt-get install -y software-properties-common; \  
apt-add-repository -y ppa:ondrej/php; \  
apt-key adv --recv-key --keyserver hkp://keyserver.ubuntu.com:80
4F4EA0AAE5267A6C; \  
apt-get clean  
  
RUN apt-get update; \  
apt-get install -y \  
curl \  
wget \  
vim \  
nodejs \  
mysql-client \  
nmap \  
libcurl4-openssl-dev \  
git-core \  
apache2 \  
apache2-bin \  
libapache2-mod-php7.0 \  
libapache2-mod-rpaf \  
php7.0 \  
php-zip \  
php-cli \  
php-curl \  
php-mbstring \  
php-intl \  
php-gd \  
php7.0-dev \  
php-mysql \  
php-pear \  
php-memcache \  
php-sqlite3 \  
dh-php \  
build-essential \  
php-pear \  
php-mbstring; \  
apt-get clean  
  
################################################################################  
  
#################################---COMMAND---##################################  
  
CMD bash  
  
################################################################################  

