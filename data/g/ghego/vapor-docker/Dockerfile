FROM ubuntu:15.10  
MAINTAINER Matteo Crippa @ghego20  
EXPOSE 8888  
RUN mkdir -p /var/www/app  
ENV WEB /var/www/app  
VOLUME ${WEB}  
RUN apt-get update; apt-get update -y; apt-get install curl wget -y  
RUN curl -sL swift.vapor.sh/ubuntu | bash  

