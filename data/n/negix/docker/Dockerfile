#Dockerfile  
FROM ubuntu:latest  
MAINTAINER negix "negix@sina.com"  
ENV REFRESHED_AT 2017-08-01  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am in your container' \  
>/usr/share/nginx/html/index.html  
CMD ["/bin/bash"]  
EXPOSE 80  

