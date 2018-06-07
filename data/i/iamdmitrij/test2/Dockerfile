FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
CMD nginx  
  
EXPOSE 80  
VOLUME /var/www/html

