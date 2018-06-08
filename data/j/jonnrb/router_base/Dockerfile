from ubuntu:xenial as cbuild  
run apt-get update \  
&& apt-get install -y build-essential libnfnetlink-dev bison flex curl \  
&& curl -q -O -L ftp://ftp.netfilter.org/pub/iptables/iptables-1.4.21.tar.bz2
\  
&& tar xf iptables-1.4.21.tar.bz2 \  
&& cd iptables-1.4.21 \  
&& ./configure --enable-static --disable-shared \  
&& make \  
&& make install  
  
from golang:1.9 as gobuild  
add . /go/src/github.com/jonnrb/network_containers/router_base  
run cd /go/src/github.com/jonnrb/network_containers/router_base/cmd/init \  
&& CGO_ENABLED=0 GOOS=linux go-wrapper download \  
&& CGO_ENABLED=0 GOOS=linux go-wrapper install  
  
from gcr.io/distroless/base  
copy \--from=cbuild /usr/local/sbin/xtables-multi /sbin/iptables  
copy \--from=gobuild /go/bin/init /init  
expose 8080  
healthcheck \--interval=10s --timeout=5s cmd ["/init", "-health_check"]  
entrypoint ["/init"]  
  
# Get required packages  
#run apk update && apk add iptables  
#add iptables.tmpl /data/iptables.tmpl  
#add init.sh /  
#healthcheck --timeout=3s --interval=15s --retries=4 \  
# cmd ["ping", "-c", "1", "8.8.8.8"]  
#entrypoint ["/init.sh"]  

