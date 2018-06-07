# levelonedev/indatus-website:web  
FROM levelonedev/indatus-website:base  
  
# Add vhost here so we don't have to rebuild base to apply vhost changes  
ADD containers/vhost.conf /etc/nginx/sites-available/default  
  
RUN mkdir -p /var/www  
ADD . /var/www  
  
USER root  
  
WORKDIR /var/www  
ENV LC_CTYPE=en_US.UTF-8  
RUN /var/www/build.sh && \  
chown -R www-data:www-data .  

