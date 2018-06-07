FROM alpine  
MAINTAINER Yusuf Ali "ali@yusuf.email"  
ENV PYTHON_EGG_CACHE="/config/plugins/.python-eggs"  
RUN \  
sed -i -e 's/v3\\.\d/edge/g' /etc/apk/repositories && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --no-cache --update openvpn boost-python tzdata python py-pip deluge
2> /dev/null && \  
mkdir -p /downloads /config /vpn && \  
addgroup -g 1000 abc && \  
adduser -DH -G abc -g "" -s /bin/sh -h /config abc && \  
pip install incremental constantly packaging automat  
  
ADD root/ /  
EXPOSE 8112 58846 58946 58946/udp  
VOLUME /config /downloads /vpn  
  
ENTRYPOINT ["/root/startup"]  

