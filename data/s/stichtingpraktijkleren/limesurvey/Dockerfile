FROM php:7-apache  
  
RUN apt-get update && \  
apt-get upgrade -q -y  
  
RUN apt-get install -q -y libpng-dev && \  
docker-php-ext-install gd  
  
RUN apt-get install -y sendmail libc-client-dev libkrb5-dev && \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-install imap  
  
RUN apt-get install -q -y curl libssl-dev libcurl4-openssl-dev pkg-config && \  
docker-php-ext-configure curl --with-libdir=lib/x86_64-linux-gnu --with-
openssl=/usr --with-curl && \  
docker-php-ext-install curl  
  
RUN apt-get install -q -y libldap2-dev && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get install -y zlib1g-dev && \  
docker-php-ext-install zip  
  
RUN rm -r /var/lib/apt/lists/* && \  
apt-get clean  
  
COPY ./src /src  
  
RUN rm -rf /var/www/html \  
&& mv /src /var/www/html \  
&& chmod -R 755 /var/www/html/tmp ; chown -R www-data /var/www/html/tmp \  
&& chmod -R 755 /var/www/html/upload ; chown -R www-data /var/www/html/upload
\  
&& chmod -R 755 /var/www/html/application/config/ ; chown -R www-data
/var/www/html/application/config/  

