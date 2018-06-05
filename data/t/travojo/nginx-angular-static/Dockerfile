# Pull base image.  
FROM kyma/docker-nginx  
  
# File Author.  
MAINTAINER Robert Hänsel <robert@advalyze.de>  
  
# Overwrite cfg  
COPY etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default  
  
# Define working directory.  
WORKDIR /var/www  
  
# Define default command.  
CMD 'nginx'  

