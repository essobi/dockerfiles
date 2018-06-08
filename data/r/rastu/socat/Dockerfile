FROM alpine:3.5  
ENV SOCAT_VERSION 1.7.3.1-r1  
  
RUN apk --no-cache add socat=${SOCAT_VERSION}  
  
ENTRYPOINT ["/usr/bin/socat"]

