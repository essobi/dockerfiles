FROM alpine:3.4  
RUN apk add --no-cache bash \  
curl  
  
COPY crl.sh /  
  
ENTRYPOINT ["/crl.sh"]  

