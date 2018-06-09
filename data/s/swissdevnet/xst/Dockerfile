FROM alpine:latest  
COPY xmr-stak /  
COPY config.txt /  
RUN apk --no-cache upgrade \  
&& apk --no-cache add \  
openssl  
ENTRYPOINT ["./xmr-stak"]  

