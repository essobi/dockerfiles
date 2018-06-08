FROM ubuntu  
  
MAINTAINER Johannes <johannes@number13.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV ADMIN_PW adminpassword12  
  
RUN apt-get update && apt-get install -y -qq \  
nginx \  
ca-certificates \  
php-fpm php-mysql php-imap php-mbstring \  
wget \  
mysql-client dovecot-core  
  
ADD start.sh start.sh  
ADD config_files config_files  
ADD init_db.sql init_db.sql  
RUN chmod +x start.sh  
  
ADD
https://downloads.sourceforge.net/project/postfixadmin/postfixadmin/postfixadmin-3.0/postfixadmin-3.0.tar.gz
/  
RUN tar -xvzf postfixadmin-3.0.tar.gz  
RUN rm postfixadmin-3.0.tar.gz  
RUN rm -rf /var/www/html  
RUN cp -R postfixadmin-3.0 /var/www/html  
  
RUN chmod -R g+w /var/www/html  
RUN chown -R www-data:www-data /var/www  
  
RUN service dovecot stop  
  
EXPOSE 80 443  
CMD ./start.sh

