FROM ubuntu:latest  
MAINTAINER LauLe "vanlau.le@gmail.com"  
USER root  
  
RUN apt-get update  
RUN apt-get install -y nginx  
  
RUN rm -v /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/  
ADD domain.com /var/www/  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
EXPOSE 80  
  
CMD /etc/init.d/nginx start  

