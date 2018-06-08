FROM gliderlabs/alpine:3.1  
MAINTAINER Kyle Kelley <kyle.kelley@rackspace.com>  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
ADD racknet /usr/bin/racknet  
  
ENTRYPOINT ["/usr/bin/racknet"]  

