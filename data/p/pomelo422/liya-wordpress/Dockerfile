# Based on Alpine  
# https://github.com/ngineered/nginx-php-fpm/blob/master/Dockerfile  
FROM richarvey/nginx-php-fpm:latest  
  
MAINTAINER pomelo422 <liki.du@outlook.com>  
  
# Install mysql-client and packages to support tput in run.sh  
RUN apk update  
RUN apk add --no-cache ncurses \  
mysql-client  
  
# Copy run.sh and install wp-cli  
WORKDIR /var/www/app  
ADD run.sh /run.sh  
RUN curl \  
-o /usr/bin/wp https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \  
chmod 755 /usr/bin/wp && chmod 755 /run.sh  
  
# Copy wordpress.conf to support url rewrite for nginx  
ADD wordpress.conf /etc/nginx/wordpress.conf  
  
# Run the server  
EXPOSE 80 443  
CMD ["/run.sh"]

