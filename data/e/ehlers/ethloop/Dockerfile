# ethloop - virtual RJ45 loopback plug  
  
FROM alpine  
  
COPY ethloop.c /root/  
  
RUN set -ex \  
&& cd /root \  
&& apk add --update-cache libpcap \  
&& apk add --virtual build-deps gcc musl-dev libpcap-dev \  
&& gcc -Wall -O2 -s -o /usr/local/bin/ethloop ethloop.c -lpcap \  
&& apk del build-deps \  
&& rm -rf /var/cache/apk/* \  
#  
# startup script  
#  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
\x23 on eth0 disable IPv6, set MTU to 9000\n\  
ip link set dev eth0 down\n\  
sysctl -q -w net.ipv6.conf.eth0.disable_ipv6=1\n\  
ip link set dev eth0 mtu 9000\n\  
ip link set dev eth0 up\n\  
\n\  
ethloop eth0' \  
> /etc/init.sh && chmod +x /etc/init.sh  
  
CMD [ "/etc/init.sh" ]  

