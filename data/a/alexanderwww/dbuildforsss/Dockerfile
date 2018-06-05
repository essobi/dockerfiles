FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y wget unzip git  
ADD CHECKSUM-go1.6.2.linux-amd64 /root/go/CHECKSUM-go1.6.2.linux-amd64  
RUN cd ~/go && wget https://storage.googleapis.com/golang/go1.6.2.linux-
amd64.tar.gz && sha256sum -c CHECKSUM-go1.6.2.linux-amd64 && tar xf
go1.6.2.linux-amd64.tar.gz  
RUN cd && export GOROOT="$PWD/go/go" && mkdir gopath && cd gopath && export
GOPATH="$PWD" && ~/go/go/bin/go get github.com/alicewww/shadowsocks-
go/cmd/shadowsocks-server  
ADD ss-run.sh /usr/bin/ss-run.sh  
ADD ss-rotate.sh /usr/bin/ss-rotate.sh  
ADD ss-cron /etc/cron.d/ss-cron  
VOLUME /ss  
ENTRYPOINT ["/usr/bin/ss-run.sh"]  

