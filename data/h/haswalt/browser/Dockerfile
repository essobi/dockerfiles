FROM alpine:3.3  
RUN apk add --update php-fpm php-json nginx ca-certificates bash  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
WORKDIR /srv  
  
ADD src /srv  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD entrypoint.sh /entrypoint.sh  
  
RUN mkdir /volumes  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  

