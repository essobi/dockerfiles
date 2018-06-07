FROM ubuntu:latest  
MAINTAINER Earncef Sequeira <earncefs@yahoo.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
ENV MYSQL_ROOT_PASSWORD root  
  
RUN \  
apt-get update && \  
apt-get install -y apache2 && \  
apt-get install -y mysql-server && \  
apt-get -y install php libapache2-mod-php php-mcrypt php-mysql php-cli php-
curl php-gd php-zip php-soap php-xml php-intl php-mbstring && \  
apt-get -y install postfix nano zip unzip curl git wget && \  
phpenmod mcrypt && \  
a2enmod rewrite && \  
sed -i -e 's/DirectoryIndex index.html index.cgi index.pl index.php
index.xhtml index.htm/DirectoryIndex index.php index.html/g'
/etc/apache2/mods-available/dir.conf && \  
sed -i -e 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf
&& \  
cd /tmp && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer && \  
wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
cd / && \  
rm -rf /tmp/composer && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /var/www/html  
  
EXPOSE 80 3306  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
ENTRYPOINT service mysql start && service apache2 start && /bin/bash  

