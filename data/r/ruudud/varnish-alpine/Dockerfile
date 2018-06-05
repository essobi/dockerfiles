FROM alpine:3.4  
MAINTAINER Pål Ruud <ruudud@gmail.com>  
  
RUN apk --no-cache add varnish  
  
EXPOSE 80  
ENTRYPOINT ["varnishd"]  
CMD ["-j unix,user=varnish", "-F", "-f", "/etc/varnish/default.vcl", "-s
malloc,100m"]  

