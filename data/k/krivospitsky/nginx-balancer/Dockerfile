FROM debian:wheezy  
MAINTAINER Alexandr Krivospitsky <alex@krivospitsky.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y upgrade && apt-get -y install nginx && apt-
get clean  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
  
  
CMD ["nginx"]  

