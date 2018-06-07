FROM alpine:3.3  
MAINTAINER Jeremy Wells <jemmyw@gmail.com>  
  
RUN apk update \  
&& apk add jq  
  
RUN mkdir /app  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/jq"]  

