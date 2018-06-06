FROM alpine:3.5  
LABEL maintainer "kazuki.matsuda@intimatemerger.com"  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --no-cache dante-server  
  
ADD sockd.conf /etc/sockd.conf  
  
EXPOSE 1080  
ENTRYPOINT ["/usr/sbin/sockd"]  

