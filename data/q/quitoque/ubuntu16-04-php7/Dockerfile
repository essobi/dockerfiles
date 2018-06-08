FROM quitoque/ubuntu16-04  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
# Update repositories  
RUN apt-get update && apt-get install -qq -y php7.0 php7.0-cli php7.0-json
php7.0-mysql \  
php7.0-xml php7.0-intl php-xdebug php7.0-gd php7.0-curl php7.0-soap \  
php7.0-zip php7.0-bcmath php7.0-mbstring mysql-client && \  
apt-get -qq -y autoremove && apt-get -qq -y autoclean && \  
apt-get -qq -y clean && rm -rf /var/lib/apt/lists/*  
  
COPY files/xdebug.ini /etc/php/7.0/mods-available/xdebug.ini  

