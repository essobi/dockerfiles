FROM gliderlabs/alpine:3.2  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
RUN apk add --update \  
jq-dev \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["jq"]  

