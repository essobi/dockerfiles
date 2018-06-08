FROM alpine:3.7  
RUN apk add --no-cache su-exec openssl ca-certificates \  
&& mkdir /ca-certificates  
  
VOLUME /ca-certificates  
  
COPY docker-entrypoint.sh /  
COPY openssl.conf /  
  
CMD [ "su-exec", "root", "/docker-entrypoint.sh" ]  

