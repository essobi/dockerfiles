FROM ubuntu  
  
MAINTAINER Matthew A. Brassey version: 0.1  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y apache2 supervisor  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY cD/ /var/www/html  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

