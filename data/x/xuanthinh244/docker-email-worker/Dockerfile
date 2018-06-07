# User imager from phalcon 3.0  
FROM xuanthinh244/docker-phalcon:v3.0.1-DevLog  
MAINTAINER vi.nt "<vi.nt@geekup.vn>"  
# Install supervisord  
RUN apt update && apt install -y supervisor;  
  
# Copy supervisord config  
COPY docker-config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Create directory /var/www/html/app and set it as a mount point  
RUN mkdir -p /var/www/html  
ADD ./ /var/www/html  
WORKDIR /var/www/html  
  
# Install composer and run composer install  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php composer.phar install  
RUN rm composer.phar  
  
# set cmd command  
CMD ["/usr/bin/supervisord"]  

