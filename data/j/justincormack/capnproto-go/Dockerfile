FROM golang:1.7-alpine3.5  
RUN \  
apk update && apk add git make build-base curl file autoconf automake libtool
linux-headers && \  
cd /root && \  
git clone https://github.com/sandstorm-io/capnproto.git && \  
cd capnproto/c++ && \  
./setup-autotools.sh && \  
autoreconf -i && \  
./configure && \  
make -j6 check && \  
make install && \  
go get -u -t zombiezen.com/go/capnproto2 && \  
cd $GOPATH/src/zombiezen.com/go/capnproto2/capnpc-go/ && \  
go install  

