FROM islandora/claw-karaf:open-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
RUN apk-install git php-phar php-ctype php-json php-curl php-xml php-posix
php-openssl && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && \  
mv /usr/local/bin/composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer && \  
cleanup  
  
RUN git clone https://github.com/Islandora-CLAW/Alpaca.git /opt/alpaca && \  
cd /opt/alpaca/commands; composer install && \  
cd /opt/alpaca; mvn clean install -Dmaven.repo.local=${M2_HOME}/repository &&
\  
cleanup  
  
COPY rootfs /  

