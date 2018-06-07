FROM alpine  
RUN apk add --no-cache openssl netcat-openbsd  
COPY ./service.sh /usr/local/bin  
ENTRYPOINT [ "service.sh" ]  
  

