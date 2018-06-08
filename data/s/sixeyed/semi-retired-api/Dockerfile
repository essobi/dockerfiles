FROM nginx:1.9.10  
MAINTAINER Elton Stoneman <elton@sixeyed.com>  
  
RUN mkdir -p /var/www  
COPY ./www /var/www  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY ./conf/semi-retired-api.conf /etc/nginx/conf.d/

