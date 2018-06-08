FROM kevinpark/nginx-php-redis  
MAINTAINER Kevin Park<kevinpark@webace.co.kr>  
  
RUN mkdir /var/www/cfg  
  
ADD cfg /var/www/cfg  
ADD src /var/www/html  
ADD default.conf /etc/nginx/sites-available/default.conf  
  
VOLUME ["/var/www/cfg"]  
VOLUME ["/var/www/html/modules"]  
VOLUME ["/var/www/html/rester/lib"]  
VOLUME ["/var/www/html/rester/files"]  
  

