FROM nginx:1.9.3  
MAINTAINER Joachim Lusiardi  
  
RUN apt-get update; \  
apt-get install -y apache2-utils  
  
ADD nginx.conf /etc/nginx.conf  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
ENTRYPOINT /start.sh  
  

