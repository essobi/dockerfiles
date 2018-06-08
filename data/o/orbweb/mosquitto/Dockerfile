FROM alpine:edge  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
ENV VERSION 1.4.8  
RUN apk --no-cache add \  
mosquitto=$VERSION-r0  
EXPOSE 1883/tcp  
CMD ["mosquitto"]  

