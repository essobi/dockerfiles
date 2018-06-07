FROM lojassimonetti/apache2-php7-silex:latest  
  
COPY ./ /var/www/html  
ADD ./provisioning/supervisor.conf /etc/supervisor/conf.d/workers.conf  
RUN composer install  

