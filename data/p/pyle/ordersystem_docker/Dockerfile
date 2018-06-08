FROM ubuntu:14.04  
MAINTAINER Adam Pyle<adam@adampyle.net>  
  
#Basic apt  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
#App requirements  
RUN apt-get install -y \  
php5-cli php5-sqlite php5-mcrypt php5-mysql nginx php5-fpm git wget  
  
#PHP & nginx setup  
ADD php.ini /etc/php5/fpm/php.ini  
ADD nginx.conf /etc/nginx/nginx.conf  
  
#Install Composer  
RUN bash -c "wget http://getcomposer.org/composer.phar && mv composer.phar
/usr/local/bin/composer" && \  
chmod 775 /usr/local/bin/composer  
  
#Volume for apps storage on container  
#VOLUME /app/order_system/storage  
#Volume for apps public directory  
#VOLUME /app/order_system/public  
RUN git clone https://github.com/pyle/ordersystem.git /app  
RUN chmod -R 777 /app  
#Run Composer on  
WORKDIR /app/order_system  
RUN bash -c "composer install"  
#Run Migration  
RUN php /app/order_system artisan migrate  
  
EXPOSE 8000  
# ENTRYPOINT ["nginx"]  
# #CMD ["php", "/app/order_system/artisan", "serve"]  
CMD service php5-fpm restart && nginx  

