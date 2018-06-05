FROM ubuntu:latest  
  
MAINTAINER Luciano Jr <luciano@lucianojr.com.br>  
  
RUN apt update && apt install -y nginx  
  
ADD nginx.conf /etc/nginx/  
ADD attendize.conf /etc/nginx/sites-available/  
  
RUN ln -s /etc/nginx/sites-available/attendize.conf /etc/nginx/sites-
enabled/attendize  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN echo "upstream php-upstream { server php:9000; }" >
/etc/nginx/conf.d/upstream.conf  
  
RUN usermod -u 1000 www-data  
  
CMD ["nginx"]  
  
EXPOSE 80  
EXPOSE 443

