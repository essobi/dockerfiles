FROM alpine:3.2  
MAINTAINER Chris Heng <bigblah@gmail.com>  
  
RUN apk add -U bash && rm -rf /var/cache/apk/*  
  
ADD s6-2.1.6.0.tar.gz /  
ADD service /etc/service  
  
ENTRYPOINT ["/usr/bin/s6-svscan", "-t0"]  
CMD ["/etc/service"]  

