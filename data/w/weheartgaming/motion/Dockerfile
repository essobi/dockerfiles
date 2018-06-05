FROM alpine:latest  
  
LABEL maintainer "dan@whg.no"  
  
# Package is in the testing repo  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk --no-cache --update add motion \  
&& rm -rf /var/cache/apk/*  
  
# Exposing 20 ports to support more than one feed  
# 8080 is the default port  
EXPOSE 8080-8100  
CMD [ "motion", "-n" ]  

