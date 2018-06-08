# mumble-server  
#  
# Version 1.0.0  
FROM alpine:3.5  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
RUN apk add --no-cache murmur  
  
VOLUME ["/config"]  
  
ADD ["murmur.ini", "/config/murmur.ini"]  
  
EXPOSE 64738  
EXPOSE 64738/udp  
  
CMD ["murmurd", "-fg", "-ini", "/config/murmur.ini"]  

