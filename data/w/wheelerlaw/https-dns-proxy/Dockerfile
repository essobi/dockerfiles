FROM alpine:3.7  
MAINTAINER Wheeler Law <whelderwheels613@gmail.com>  
  
RUN apk update && apk add build-base curl bash iptables git c-ares-dev curl-
dev libev-dev cmake \  
&& git clone https://github.com/aarond10/https_dns_proxy.git \  
&& (cd https_dns_proxy/ && cmake .) \  
&& make -C https_dns_proxy  
  
# Use a multi-stage build to cut down on image size  
FROM alpine:3.7  
RUN apk --no-cache add iptables c-ares libcurl libev ca-certificates bash  
COPY \--from=0 https_dns_proxy/https_dns_proxy /usr/local/bin  
  
COPY entrypoint.sh /entrypoint.sh  
COPY fw.sh /fw.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

