FROM alpine:latest  
  
MAINTAINER carriera  
  
RUN apk add --no-cache nginx nano vim  
  
ADD conf/nginx.conf /etc/nginx/  
ADD conf/symfony.conf /etc/nginx/sites-enabled/  
  
RUN echo "upstream php-upstream { server php:9000; }" >
/etc/nginx/conf.d/upstream.conf  
  
WORKDIR /etc/nginx  
  
CMD ["nginx"]  
  
EXPOSE 80  
EXPOSE 443  

