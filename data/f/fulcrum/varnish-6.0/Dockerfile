# edge is 3.8 currently  
FROM alpine:edge  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
RUN echo "Cache bust 201804160000" && \  
apk update && apk upgrade && \  
apk --no-cache add varnish  
  
ENTRYPOINT ["/usr/sbin/varnishd"]  
  
CMD
["-F","-P","/run/varnish.pid","-a",":80,PROXY","-f","/etc/varnish/default.vcl","-S","/etc/varnish/secret","-T","0.0.0.0:6082","-t","120","-s","malloc,128M"]  

