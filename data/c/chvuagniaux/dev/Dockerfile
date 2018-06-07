FROM debian:stretch  
MAINTAINER Christophe Vuagniaux <cvx@cvxnet.ch>  
  
ADD composer-install.sh /tmp/composer-install.sh  
  
RUN \  
apt-get update && \  
apt-get install -y curl ca-certificates apt-transport-https --no-install-
recommends && \  
  
curl -o /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ stretch main" >>
/etc/apt/sources.list && \  
  
apt-get update && \  
apt-get install -y \  
php7.2-cli \  
php7.2-mysql php7.2-sqlite3 php7.2-curl php7.2-gd php7.2-imap php7.2-imagick \  
php7.2-json php7.2-intl php7.2-gmp php7.2-geoip php7.2-mbstring php7.2-xml
php7.2-zip \  
tmux vim zip unzip && \  
  
rm -fr /var/lib/apt/lists/* && \  
  
curl -o /usr/local/bin/phpunit -L https://phar.phpunit.de/phpunit.phar && \  
chmod +x /usr/local/bin/phpunit && \  
  
chmod +x /tmp/composer-install.sh && \  
sync && \  
/tmp/composer-install.sh && \  
rm /tmp/composer-install.sh && \  
  
chsh -s /bin/bash www-data # allow to use www-data (su www-data) with uid 33  
  
CMD ["bash"]  

