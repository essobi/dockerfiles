FROM dockette/php:7.1-fpm  
  
RUN apt-get update \  
&& apt-get -y install php7.1-mysql php7.1-gmp php7.1-cgi php7.1-cli
php7.1-curl php7.1-json php7.1-odbc php7.1-tidy php7.1-common php7.1-xmlrpc
php7.1-gd php-pear php7.1-dev php7.1-imap php7.1-mcrypt php7.1-mysqlnd
php7.1-mbstring php7.1-curl php7.1-dom php7.1-zip php7.1-soap php-xdebug git
mysql-client \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
WORKDIR "/app"  

