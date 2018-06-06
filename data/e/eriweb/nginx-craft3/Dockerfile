FROM nginx:1.11-alpine  
MAINTAINER Erik Weber <erik@vangenplotz.no>  
  
RUN echo "upstream php { server php:9000; }" > /etc/nginx/conf.d/upstream.conf  
COPY files/default /etc/nginx/conf.d/default.conf  
COPY files/nginx.conf /etc/nginx/nginx.conf  
  

