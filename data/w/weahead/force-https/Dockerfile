FROM nginx:1.11.8-alpine  
  
MAINTAINER We ahead <docker@weahead.se>  
  
RUN rm -f /etc/nginx/conf.d/*.conf  
  
COPY redirect.conf /etc/nginx/conf.d/  

