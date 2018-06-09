FROM php:5-apache  
  
RUN apt-get update && apt-get install -y unzip php5-mysql  
  
RUN curl -L http://downloads.sourceforge.net/project/lwt/lwt_v_1_6_1.zip >
/tmp/lwt.zip && \  
cd /var/www/html && \  
unzip /tmp/lwt.zip && \  
rm /tmp/lwt.zip  
  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install mbstring  
  
COPY connect.inc.php /var/www/html/  
COPY php.ini /usr/local/etc/php/  

