FROM oxkipo/apache2-php7  
MAINTAINER Kristian Drucker  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

