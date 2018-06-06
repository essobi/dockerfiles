FROM alpine  
ENV DNS_VER 1.3.2  
ENV DNS_URL
https://github.com/clowwindy/ChinaDNS/releases/download/${DNS_VER}/chinadns-${DNS_VER}.tar.gz  
ENV DNS_FILE chinadns.tar.gz  
  
RUN export BUILD_DEPS="musl-dev gcc gawk make libtool" \  
&&export RUNTIME_DEPS="curl wget git" \  
&&set -ex \  
&&apk add \--no-cache \--update $BUILD_DEPS $RUNTIME_DEPS dnsmasq \  
&& mkdir -p /chinadns \  
&& cd /chinadns \  
&& curl -sSL ${DNS_URL} -o ${DNS_FILE} \  
&& tar xzf ${DNS_FILE} \--strip 1 \  
&& ./configure \  
&& make install \  
&& rm -rf /chinadns \  
&& curl http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest | grep
ipv4 | grep CN | awk -F\| '{printf("%s/%d\n", $4, 32-log($5)/log(2))}' >
/etc/chnroute.txt \  
&& cd / \  
&& git clone \--recursive https://github.com/felixonmars/dnsmasq-china-
list.git \  
&& cp /dnsmasq-china-list/dnsmasq-update-china-list /usr/bin/ \  
&& cp /dnsmasq-china-list/accelerated-domains.china.conf /etc/dnsmasq.d/ \  
&& cp /dnsmasq-china-list/apple.china.conf /etc/dnsmasq.d/ \  
&& cp /dnsmasq-china-list/bogus-nxdomain.china.conf /etc/dnsmasq.d/ \  
&& cp /dnsmasq-china-list/google.china.conf /etc/dnsmasq.d/ \  
&& rm -rf /var/cache/apk/* \  
&& apk del \--purge $BUILD_DEPS $RUNTIME_DEPS \  
&& rm -rf /dnsmasq-china-list  
RUN echo $'\  
dnsmasq \--cache-size=25000 \--conf-file=/dev/null \--conf-dir=/etc/dnsmasq.d/
\--log-facility=/dev/stdout \--no-resolv \--server=127.0.0.1#2053 --user=root
\n\  
chinadns -b 127.0.0.1 -c /etc/chnroute.txt -m -p 2053 -s
114.114.114.114,208.67.222.222:443,8.8.4.4 -y 0.3 \n\  
'>/entrypoint.sh \  
&& chmod a+x /entrypoint.sh \  
&& sed -i '1i#!/bin/sh' /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 53/tcp 53/udp  
VOLUME /etc/dnsmasq.d/  

