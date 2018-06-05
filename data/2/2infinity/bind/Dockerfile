FROM alpine:latest  
MAINTAINER 2infinite <2infinite@users.noreply.github.com>  
RUN apk --no-cache add bind bind-tools  
CMD ["/usr/sbin/named", "-c", "/etc/bind/named.conf", "-g", "-u", "named",
"-4"]  

