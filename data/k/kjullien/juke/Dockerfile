FROM wordpress:latest  
  
RUN apt-get update && apt-get install -yq git zip unzip  
  
WORKDIR /var/www/html/wp-content/plugins  
COPY plugins ./  
  
WORKDIR /var/www/html/wp-content/themes/juke  
COPY theme ./  
  
WORKDIR /var/www/html

