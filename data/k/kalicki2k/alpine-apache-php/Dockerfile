FROM kalicki2k/alpine-apache  
  
MAINTAINER Sebastian Kalicki (https://github.com/kalicki2k)  
  
COPY Dockerfiles/. /  
  
RUN apk update && apk upgrade && \  
apk add curl git mysql-client \  
php7 php7-apache2 php7-apcu php7-bcmath php7-ctype php7-curl php7-dom
php7-fileinfo php7-gd php7-iconv php7-imap php7-intl \  
php7-json php7-mbstring php7-mcrypt php7-mysqli php7-opcache php7-openssl
php7-pgsql php7-pdo php7-pdo_mysql php7-phar \  
php7-session php7-simplexml php7-soap php7-sqlite3 php7-tidy php7-tokenizer
php7-xml php7-xmlrpc php7-xmlreader php7-xmlwriter php7-xsl php7-zip php7-zlib
&& \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chmod +x /run.sh && \  
rm -rf /var/www/localhost/htdocs/index.html && \  
rm -rf /var/www/skel/htdocs/index.html && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /var/www/localhost  
  
EXPOSE 80 443  
  
ENTRYPOINT ["/run.sh"]

