FROM php:5.3-apache  
RUN cd /tmp && git clone
https://github.com/alextselegidis/easyappointments.git  
RUN cp -R /tmp/easyappointments/src/* /var/www/html && rm -rf
/tmp/easyappointments  
COPY ./config.php /var/www/html/config.php  

