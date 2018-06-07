FROM alpine:3.2  
EXPOSE 80 443  
RUN apk add --update nginx && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /tmp/nginx/client-body  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d"]  
  
CMD ["nginx", "-g", "daemon off;"]  

