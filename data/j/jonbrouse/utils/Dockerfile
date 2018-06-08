FROM alpine  
  
RUN apk update && \  
apk add \  
mysql-client && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["mysql"]  

