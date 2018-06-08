FROM alpine:3.4  
RUN apk add --update haproxy curl ca-certificates openssl && rm -rf
/var/cache/apk/*  
RUN mkdir /templates  
COPY bin/entrypoint.sh /usr/local/bin/  
COPY bin/reload.sh /usr/local/bin/  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  
  

