FROM alpine:3.2  
MAINTAINER Chris <c@crccheck.com>  
  
ENV TCPDUMP_VERSION 4.9.0-r0  
  
RUN apk add --update \  
tcpdump==${TCPDUMP_VERSION}  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/usr/sbin/tcpdump"]  

