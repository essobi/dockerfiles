FROM golang:1.10  
LABEL maintainer Child of the Universe <childoftheuniverse@protonmail.com>  
  
# Set up protocol buffer compile pipeline  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef
-o Dpkg::Options::=--force-confold --purge install gcc libc-dev protobuf-
compiler librados-dev && apt-get -q -y clean  
RUN go get github.com/golang/protobuf/protoc-gen-go  
  
# Now, get and install the main binary  
RUN mkdir -p /go/src/github.com/childoftheuniverse  
RUN cd /go/src/github.com/childoftheuniverse; git clone
https://github.com/childoftheuniverse/cstatic.git  
RUN cd /go/src/github.com/childoftheuniverse/cstatic; protoc
--go_out=plugins=grpc:. *.proto  
RUN cd /go/src/github.com/childoftheuniverse/cstatic/config; protoc
--go_out=plugins=grpc:. *.proto  
RUN go get -v github.com/childoftheuniverse/cstatic/content_server  
  
RUN ["/usr/sbin/adduser", "--system", "--home", "/nonexistent", "--no-create-
home", "--gecos", "Static Web Content Server", "--group", "--disabled-
password", "cstatic-content"]  
VOLUME ["/etc/ceph", "/secrets"]  
USER cstatic-content  
ENTRYPOINT ["/go/bin/content_servers"]  

