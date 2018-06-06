FROM ubuntu:trusty  
  
MAINTAINER Min Zhang <zmzhuai@gmail.com>  
  
ENV DEPENDENCIES git-core build-essential autoconf libtool libssl-dev  
ENV SHADOWSOCKSDIR /tmp/shadowsocks-libev  
ENV CHINADNSDIR /tmp/chinadns  
ENV CHINADNSWORKDIR ~/chinadns  
ENV PORT 8338  
ENV DNSPORT 53  
# Set up building environment  
RUN apt-get -y update \  
&& apt-get install -y $DEPENDENCIES  
  
# Get the latest code, build and install  
RUN git clone https://github.com/shadowsocks/shadowsocks-libev.git
$SHADOWSOCKSDIR  
WORKDIR $SHADOWSOCKSDIR  
RUN ./configure \  
&& make \  
&& make install  
  
# Get the ChinaDNS code, build and install  
RUN git clone https://github.com/shadowsocks/ChinaDNS.git $CHINADNSDIR  
WORKDIR $CHINADNSDIR  
RUN chmod +x ./autogen.sh \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# Tear down building environment and delete git repository  
WORKDIR /  
RUN rm -rf $SHADOWSOCKSDIR/ \  
&& rm -rf $CHINADNSDIR/ \  
&& apt-get --purge autoremove -y $DEPENDENCIES  
  
WORKDIR /  
RUN mkdir /etc/shadowsocks-libev/ \  
&& touch /etc/shadowsocks-libev/config.json  
  
# Update chnroute.txt and start shadowsocks client and chinadns  
WORKDIR $CHINADNSWORKDIR  
RUN apt-get install -y curl  
RUN curl 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest' |
grep ipv4 | grep CN | awk -F\| '{ printf("%s/%d\n", $4, 32-log($5)/log(2)) }'
> chnroute.txt  
#&& ss-local -c /etc/shadowsocks-libev/config.json -u -f /var/run/ss-local.pid
\  
#&& ss-tunnel -c /etc/shadowsocks-libev/config.json -u -l 5300 -L 8.8.4.4:53
-f /var/run/ss-tunnel.pid \  
#&& chinadns -m -c ./chnroute.txt -s
119.233.255.229,58.22.96.66,127.0.0.1:5300  
# Port in the json config file won't take affect. Instead we'll use 8388.  
#EXPOSE $PORT  
EXPOSE $DNSPORT/udp  
  
# Override the host and port in the config file.  
#ADD entrypoint /  
#ENTRYPOINT ["/entrypoint"]  
#CMD ["-h"]]  

