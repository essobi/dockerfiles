# PHP Image with apache installed  
FROM php:7-apache  
  
# Updating repositories, installing sendmail and cleaning up  
RUN apt-get update && apt-get upgrade -y sendmail && rm -rf
/var/lib/apt/lists/*  
  
# Copy website source into the published folder  
COPY src/ /var/www/html/  
  
# Copy php ini to the conf dir to enable sendmail  
COPY conf/php.ini /usr/local/etc/php/conf.d/  
  
# Run the setup script  
COPY conf/setup.sh /root/  
CMD /bin/bash /root/setup.sh  
  
#Something new  

