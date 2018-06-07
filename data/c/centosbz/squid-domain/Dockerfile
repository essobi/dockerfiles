FROM debian:stretch  
LABEL maintainer "admin@centos.bz"  
RUN apt-get update && apt-get -y install squid && rm -rf /var/lib/apt/lists/*  
RUN sed -i '/http_access deny all/i\acl Safe_domain dstdomain .github.com\nacl
Safe_domain dstdomain .amazonaws.com\nhttp_access allow Safe_domain'
/etc/squid/squid.conf  
ENTRYPOINT ["squid", "-N"]  
EXPOSE 3128

