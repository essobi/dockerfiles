FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
# install dependencies  
RUN apk --no-cache add openssl curl socat  
  
# install acme.sh  
ENV LE_VERSION 2.7.8  
RUN curl -s
"https://raw.githubusercontent.com/Neilpang/acme.sh/${LE_VERSION}/acme.sh" >
/usr/local/bin/acme.sh &&\  
chmod +x /usr/local/bin/acme.sh  
  
ENTRYPOINT ["/usr/local/bin/acme.sh"]  

