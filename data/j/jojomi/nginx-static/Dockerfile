FROM alpine:latest  
MAINTAINER Johannes Mitlmeier <dev.jojomi@yahoo.com>  
  
RUN apk add --update \  
nginx \  
&& rm -rf /var/cache/apk/*  
RUN adduser www-data -G www-data -H -s /bin/false -D && mkdir /tmp/nginx/  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD default.conf /etc/nginx/sites-enabled/default  
  
EXPOSE 80  
EXPOSE 443  
VOLUME ["/var/www", "/var/log/nginx"]  
WORKDIR /etc/nginx  
  
CMD ["nginx"]  

