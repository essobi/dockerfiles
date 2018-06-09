FROM php:7.0-apache  
  
# noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY icecoder /var/www/html  
  
RUN apt-get update && apt-get install -y wget unzip  
  
RUN wget https://github.com/icecoder/ICEcoder/archive/v6.0.zip && \  
unzip v6.0.zip && \  
cp -rp ICEcoder-6.0/* /var/www/html/ && \  
rm v6.0.zip  
  
RUN chown -R www-data:www-data /var/www/html  
  
RUN ls -l /var/www/html  
  
EXPOSE 80

