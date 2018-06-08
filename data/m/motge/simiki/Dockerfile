FROM alpine:latest  
  
LABEL maintainer "mail@mueller-martin.net"  
  
RUN apk add --no-cache python3 && pip3 install simiki  
RUN mkdir /wiki  
  
WORKDIR /wiki  
  
ENTRYPOINT ["simiki"]  

