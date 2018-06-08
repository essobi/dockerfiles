FROM ubuntu:14.04  
MAINTAINER Docker Education Team <education@docker.com>  
  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am in your container' \  
>/usr/share/nginx/html/index.html  
  
# March test  
RUN echo 'My name is March . Hello World'  
  
CMD [ "nginx", "-g", "daemon off;" ]  
  
EXPOSE 80  

