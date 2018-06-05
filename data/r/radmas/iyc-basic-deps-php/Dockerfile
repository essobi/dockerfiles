FROM ubuntu:trusty  
  
MAINTAINER fernando.moro@radmas.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# BUILD TOOLS  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y \  
byobu \  
curl \  
git \  
htop \  
man \  
unzip \  
vim \  
wget \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# PHP  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
language-pack-en-base && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
  
RUN \  
add-apt-repository -y ppa:ondrej/php5-5.6  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
php5-dev \  
php5-cli \  
php5-json \  
php5-curl \  
php5-intl \  
php5-gd \  
php-apc \  
php5-gearman \  
gearman-job-server \  
php-pear \  
php5-fpm \  
php5-redis && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
pecl install mongo-1.6.7  
  
RUN \  
touch /etc/php5/mods-available/mongo.ini && \  
echo "extension=mongo.so" > /etc/php5/mods-available/mongo.ini && \  
php5enmod mongo  
  
#################################################  
  
CMD ["/bin/bash"]  

