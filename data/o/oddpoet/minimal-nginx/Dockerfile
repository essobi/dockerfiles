#==============================================================================  
# minimal nginx  
#==============================================================================  
FROM oddpoet/alpine-base:3.6  
MAINTAINER yunsang.choi<oddpoet@gmail.com>  
  
  
# install nginx  
ENV NGINX_VERSION "1.12.0-r2"  
RUN apk --update add "nginx=${NGINX_VERSION}"  
  
# mkdir for nginx.pid  
RUN mkdir -p /run/nginx  

