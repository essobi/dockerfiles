FROM nginx:1.12.2  
MAINTAINER Thomas CASTELLY <thomas@tcy.io>  
  
RUN rm -f /etc/nginx/conf.d/*  
COPY /conf/ /etc/nginx/  
  
RUN mkdir /etc/nginx/logs  
RUN touch /etc/nginx/logs/static.log  
  
RUN mkdir /tmp/nginx  
  
EXPOSE 80 443  

