FROM ubuntu:16.04  
  
MAINTAINER Pierre-Yves Guerder <pierreyves.guerder@gmail.com>  
  
# Set correct environment variables  
ENV HOME /root  
  
# MYSQL ROOT PASSWORD  
ARG MYSQL_ROOT_PASS=root  
  
RUN echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
software-properties-common \  
python-software-properties \  
build-essential \  
curl \  
git \  
unzip \  
mcrypt \  
wget \  
openssl \  
ssh \  
autoconf \  
g++ \  
make \  
locales \  
\--no-install-recommends  
  
# Ensure UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
# OpenSSL  
RUN mkdir -p /usr/local/openssl/include/openssl/ && \  
ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \  
mkdir -p /usr/local/openssl/lib/ && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/  
# MYSQL  
# /usr/bin/mysqld_safe  
RUN bash -c 'debconf-set-selections <<< "mysql-server-5.7 mysql-
server/root_password password $MYSQL_ROOT_PASS"' && \  
bash -c 'debconf-set-selections <<< "mysql-server-5.7 mysql-
server/root_password_again password $MYSQL_ROOT_PASS"' && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qqy mysql-server-5.7 \--no-
install-recommends  
  
# PHP Extensions  
RUN add-apt-repository -y ppa:ondrej/php && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq npm less composer sudo
apache2 libapache2-mod-php7.2 php-pear php7.2-mysql php7.2-dev php7.2-zip
php7.2-xml php7.2-mbstring php7.2-curl php7.2-json php7.2-mysql
php7.2-tokenizer php7.2-cli php7.2-imap php7.2-intl php7.2-gd php7.2-xdebug &&
\  
DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y g++ build-essential
make php7.1 libapache2-mod-php7.1 autoconf && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Node libraries  
RUN npm install -g bower bower uglifycss uglify-js  
  
# Timezone & memory limit  
RUN echo "date.timezone=Europe/Berlin" >
/etc/php/7.2/cli/conf.d/date_timezone.ini && echo "memory_limit=1G" >>
/etc/php/7.2/apache2/php.ini  
  
# Goto temporary directory.  
WORKDIR /tmp  

