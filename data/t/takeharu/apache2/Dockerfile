FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y apache2  
  
#enable module  
RUN a2enmod rewrite ssl  
  
#port  
EXPOSE 80 443  
CMD ["apachectl", "-DFOREGROUND"]  

