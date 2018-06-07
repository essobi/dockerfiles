FROM alpine:3.4  
RUN apk add --update exiv2 \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["exiv2"]  

