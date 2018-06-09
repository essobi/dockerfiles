FROM stepansib/php-js-symfony-oro:7.1  
MAINTAINER Stepan Yudin <stepan.sib@gmail.com>  
  
ENV REFRESHED_AT 2017–09-21  
# Install Nginx and Supervisor  
RUN apt-get install nginx supervisor -yqq  
  
# Configure NGINX main settings  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./host.conf /etc/nginx/sites-available/default  
  
# Configure supervisor  
COPY ./supervisor.conf /etc/supervisor/conf.d/php-nginx-supervisor.conf  
  
# Enable connection to PHP from localhost  
RUN sed -i 's/;listen.allowed_clients = 127.0.0.1/listen.allowed_clients =
127.0.0.1/' /usr/local/etc/php-fpm.d/www.conf  

