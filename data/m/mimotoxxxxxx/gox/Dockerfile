FROM ubuntu  
WORKDIR /root  
RUN apt-get update -y -qq && apt-get install -y -qq wget tar unzip gcc git
mercurial  
ENV GOROOT /root/go  
ENV GOPATH /root/gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
ENV GOVER 1.3rc1  
RUN \  
mkdir gopath && \  
wget -nv http://golang.org/dl/go$GOVER.linux-amd64.tar.gz && \  
tar zxf go$GOVER.linux-amd64.tar.gz && \  
rm go$GOVER.linux-amd64.tar.gz && \  
go get github.com/mitchellh/gox && \  
go get github.com/inconshreveable/gonative  
ENV PLATFORMS linux_386 linux_amd64 darwin_386 darwin_amd64 windows_386
windows_amd64 freebsd_386 freebsd_amd64  
RUN \  
mkdir -p /usr/local/gonative && cd /usr/local/gonative && gonative
-version=$GOVER -platforms="$PLATFORMS"  

