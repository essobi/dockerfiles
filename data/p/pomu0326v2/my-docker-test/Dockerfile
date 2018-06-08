FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y nginx  
  
COPY ./default /etc/nginx/sites-available/default  
COPY ./html /var/www/html  
  
CMD ["nginx", "-g", "daemon off;"]

