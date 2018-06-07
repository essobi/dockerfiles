# emirb/php72 is used because php:7.2-rc-cli uses an old version of ca-
certificates preventing openjdk-8-jdk-headless from being installed  
FROM emirb/php72  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
php7.2-pdo \  
openjdk-8-jdk-headless \  
mysql-client \  
sudo \  
vim \  
ant \  
git \  
rsync \  
unzip \  
netcat-openbsd \  
&& apt-get purge -y --auto-remove && apt-get clean all && rm -rf /var/lib/apt/
\  
&& useradd -ms /bin/bash shopware  
  
COPY shopware.ini /usr/local/etc/php/conf.d/shopware.ini  
COPY wait.sh /tmp/wait.sh  
RUN chmod +x /tmp/wait.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR /var/www/html  

