FROM phusion/baseimage:latest  
  
RUN apt-get update -y  
  
RUN add-apt-repository -y ppa:ondrej/php5-5.6  
  
RUN apt-get update  
  
RUN apt-get -y install php5-fpm \  
php5-curl php5-gd php5-mcrypt \  
php5-cli php-pear --force-yes  
  
RUN pecl install mongo  
RUN echo "extension=mongo.so" >> /etc/php5/mods-available/mongo.ini  
RUN echo "extension=mongo.so" >> /etc/php5/fpm/conf.d/20-mongo.ini  
RUN echo "extension=mongo.so" >> /etc/php5/cli/conf.d/20-mongo.ini  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/cli/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;daemonize = yes/daemonize = no/" /etc/php5/fpm/php-fpm.conf  
RUN sed -i "s%listen = /var/run/php5-fpm.sock%listen = 0.0.0.0:9000%"
/etc/php5/fpm/pool.d/www.conf  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

