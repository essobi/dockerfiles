FROM alpine:3.3  
MAINTAINER Lance Chen <cyen0312@gmail.com>  
  
RUN adduser -S -G abuild abuild  
  
RUN apk update \  
&& apk add alpine-sdk \  
&& rm -rf /vaar/cache/apk/*  
  
USER abuild  
WORKDIR /build  
CMD abuild checksum && abuild -r  

