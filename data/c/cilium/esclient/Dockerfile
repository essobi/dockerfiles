FROM alpine:3.6  
LABEL maintainer tgraf@tgraf.ch  
  
RUN \  
apk add --update curl build-base bash tcpdump strace bind-tools iproute2 net-
tools iputils && \  
curl -LO
https://github.com/HewlettPackard/netperf/archive/netperf-2.7.0.tar.gz && \  
tar -xzf netperf-2.7.0.tar.gz && \  
cd netperf-netperf-2.7.0 && ./configure --prefix=/usr && make && make install
&& \  
rm -rf netperf-netperf-2.7.0 netperf-2.7.0.tar.gz && \  
rm -f /usr/share/info/netperf.info && \  
strip -s /usr/bin/netperf /usr/bin/netserver && \  
apk del build-base && rm -rf /var/cache/apk/*  
  
CMD ["/usr/bin/netserver", "-D"]  

