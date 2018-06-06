FROM ubuntu:16.04  
# Install all the necessary packages for php 7.0  
RUN apt-get update -y  
RUN apt-get install -y php7.0-fpm php7.0-odbc php7.0-dev php7.0-mcrypt
php7.0-mysql php7.0-sybase libmysqlclient-dev\  
freetds-dev php7.0-odbc php7.0-curl php7.0-pdo-firebird php7.0 php7.0-mbstring  
  
RUN phpenmod pdo_mysql pdo_dblib mcrypt odbc pdo_odbc mysql curl  
  
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php/7.0/fpm/php-
fpm.conf  
RUN sed -e 's/;listen\\.owner/listen.owner/' -i
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -e 's/;listen\\.group/listen.group/' -i
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -e 's/listen =.*/listen = 0.0.0.0:9000/' -i
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -e 's/;request_terminate_timeout.*/request_terminate_timeout = 180;/'
-i /etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -e 's/;\s*tds version = 4\\.2/tds version = 8.0/' -i
/etc/freetds/freetds.conf  
RUN sed -e 's/error_reporting = .*/error_reporting = E_ALL/' -i
/etc/php/7.0/fpm/php.ini  
RUN sed -e 's/display_errors = .*/display_errors = On/' -i
/etc/php/7.0/fpm/php.ini  
RUN sed -e 's/display_startup_errors = .*/display_startup_errors = On/' -i
/etc/php/7.0/fpm/php.ini  
  
# Start php7-fpm service to create pid file needed to run php7-fpm  
RUN service php7.0-fpm start  
  
EXPOSE 9000  
CMD ["/usr/sbin/php-fpm7.0"]  

