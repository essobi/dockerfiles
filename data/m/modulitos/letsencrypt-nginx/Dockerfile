FROM nginx  
# FROM nginx:stable-alpine  
MAINTAINER Lucas Swart "luke@lukeswart.net"  
RUN apt-get update  
RUN apt-get install -y procps  
  
COPY start.sh /  
COPY nginx.conf /etc/nginx/  
COPY nginx-secure.conf /etc/nginx/  
  
COPY dhparams.pem /etc/ssl/private/  
CMD /start.sh  

