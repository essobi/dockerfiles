FROM alpine  
  
RUN apk update && \  
apk add ca-certificates && \  
update-ca-certificates && \  
apk add openssl && \  
rm -rf /var/cache/apk/*  

