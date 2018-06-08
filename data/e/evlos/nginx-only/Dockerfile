FROM ubuntu:saucy  
  
MAINTAINER Evlos <4tyle8@gmail.com>  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD default /etc/nginx/sites-available/default  
ADD index.html /var/www/index.html  
  
EXPOSE 80  
CMD ["nginx"]  

