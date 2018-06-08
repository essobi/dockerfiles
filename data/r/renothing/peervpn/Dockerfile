FROM alpine as builder  
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g;s/http/https/g'
/etc/apk/repositories && apk upgrade --update && \  
RUN apk upgrade --update && \  
apk add --no-cache --virtual /tmp/.build-deps \  
libressl \  
libressl-dev \  
zlib \  
zlib-dev \  
git \  
gcc \  
make \  
linux-headers \  
musl-dev \  
musl-utils \  
build-base \  
abuild \  
binutils \  
bash && \  
rm -rfv /var/cache/apk/* && \  
git clone https://github.com/peervpn/peervpn.git /tmp/peervpn.git && \  
cd /tmp/peervpn.git && \  
CFLAGS=-Wall make -j$(getconf _NPROCESSORS_ONLN) && \  
cp peervpn /sbin/peervpn && \  
install -m 755 peervpn /sbin/peervpn && \  
cd / && \  
rm -rf /tmp/peervpn.git && \  
apk del --purge -r /tmp/.build-deps  
FROM alpine  
LABEL author='renothing' role='vpn' tags='peervpn' description='peervpn based
on alpine'  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
TIMEZONE="Asia/Shanghai"  
RUN apk update && \  
apk add tzdata iproute2 dhclient dnsmasq && \  
rm -rfv /var/cache/apk/*  
COPY \--from=builder /sbin/peervpn /sbin/peervpn  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

