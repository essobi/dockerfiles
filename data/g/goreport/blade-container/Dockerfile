FROM silintl/php7  
RUN apt-get update  
RUN apt-get -y install curl git  
  
ENV REFRESHED_AT 2016-06-09  
# Copy an Apache vhost file into sites-enabled. This should map  
# the document root to whatever is right for your app  
COPY vhost-config.conf /etc/apache2/sites-enabled/  
  
RUN mkdir -p /var/www/  
RUN mkdir -p /var/www/  
WORKDIR /var/www/blade  
  
EXPOSE 80  

