FROM alpine:3.7  
LABEL org.label-schema.vcs-url="https://github.com/gpupo/container-
orchestration.git" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="gpupo" \  
org.label-schema.name="container-orchestration" \  
org.label-schema.description="Image with NGINX and Alpine" \  
org.label-schema.url="https://github.com/gpupo/container-orchestration"  
  
RUN apk add --update nginx curl vim git;\  
rm -rf /var/cache/apk/* && rm -rf /tmp/*;  
  
ADD nginx.conf /etc/nginx/  
ADD app.conf /etc/nginx/conf.d/  
  
RUN echo "upstream php-upstream { server php:9001; }" >
/etc/nginx/conf.d/upstream.conf; \  
adduser -D -g '' -G www-data www-data;  
  
CMD ["nginx"]  
  
EXPOSE 80  
EXPOSE 443  

