FROM tapsy/drupal-php-fpm:latest  
RUN addgroup --gid 501 ci && \  
useradd -g 501 -u 500 -m ci && \  
  
php -r "readfile('https://s3.amazonaws.com/files.drush.org/drush.phar');" >
/usr/bin/drush && chmod +x /usr/bin/drush && \  
  
apt-get update && apt-get install -y git apt-transport-https gettext build-
essential curl python software-properties-common libssl-dev libfontconfig1
fontconfig libfontconfig1-dev libfreetype6-dev mysql-client && \  
(curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer) && \  
  
apt-key adv --keyserver keyserver.ubuntu.com --recv 68576280 && \  
apt-add-repository "deb https://deb.nodesource.com/node_5.x $(lsb_release -sc)
main" && \  
apt-get update && apt-get install -y nodejs && \  
  
npm install -g bower  
COPY profile /root/.profile  
WORKDIR /var/www/html  
CMD sh  

