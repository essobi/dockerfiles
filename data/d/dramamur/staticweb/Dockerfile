FROM ubuntu:14.04  
MAINTAINER Docker Education Team <education@docker.com>  
  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am in your docker container this is for testing purpose in
this class' \  
>/usr/share/nginx/html/index.html  
  
CMD [ "nginx", "-g", "daemon off;" ]  
  
EXPOSE 80  

