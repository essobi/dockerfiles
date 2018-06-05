FROM ubuntu:14.04  
RUN apt-get update  
RUN sudo apt-get install -y wget unzip git privoxy squid3 haproxy python2.7  
ADD checksum /root/build/checksum  
  
RUN cd ~/build && wget https://storage.googleapis.com/golang/go1.6.2.linux-
amd64.tar.gz && sha256sum -c checksum && tar xf go1.6.2.linux-amd64.tar.gz  
RUN cd && mkdir gopath  
RUN cd && export GOROOT="$PWD/build/go" && cd gopath && export GOPATH="$PWD"
&& ~/build/go/bin/go get github.com/alicewww/shadowsocks-go/cmd/shadowsocks-
local  
  
RUN sed -i "s#^listen-address.*#listen-address 127.0.0.1:10002#"
/etc/privoxy/config && echo 'forward-socks5 / 127.0.0.1:10001 .'
>>/etc/privoxy/config  
RUN sed -i "s#^ENABLED=0#ENABLED=1#" /etc/default/haproxy  
  
ADD haproxy /usr/sbin/haproxy  
ADD squid.conf /etc/squid3/squid.conf  
ADD ss-run.py /usr/bin/ss-run.py  
ADD ss-rotate.sh /usr/bin/ss-rotate.sh  
ADD ss-cron /etc/cron.d/ss-cron  
VOLUME /ss  
ENTRYPOINT ["/usr/bin/ss-run.py"]  

