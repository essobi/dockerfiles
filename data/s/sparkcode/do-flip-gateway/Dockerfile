FROM alpine:latest  
MAINTAINER Dan Harris <daniel@sparkcode.co.uk>  
  
RUN apk update \  
&& apk add bash curl  
  
COPY floating-ip-gateway.sh /  
  
CMD /floating-ip-gateway.sh  

