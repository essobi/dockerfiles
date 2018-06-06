FROM golang:1.10  
LABEL maintainer Child of the Universe <childoftheuniverse@protonmail.com>  
  
# Set up protocol buffer compile pipeline  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef
-o Dpkg::Options::=--force-confold --purge install gcc libc-dev protobuf-
compiler librados-dev ceph-common && apt-get -q -y clean  
RUN go get github.com/golang/protobuf/protoc-gen-go  
  
# Now, get and install the main binary  
RUN mkdir -p /go/src/github.com/childoftheuniverse  
RUN cd /go/src/github.com/childoftheuniverse; git clone
https://github.com/childoftheuniverse/cstatic.git  
RUN cd /go/src/github.com/childoftheuniverse/cstatic; protoc
--go_out=plugins=grpc:. *.proto  
RUN cd /go/src/github.com/childoftheuniverse/cstatic/config; protoc
--go_out=plugins=grpc:. *.proto  
RUN go get -v github.com/childoftheuniverse/cstatic/upload_server  
  
RUN ["/usr/sbin/adduser", "--system", "--home", "/nonexistent", "--no-create-
home", "--gecos", "Static Web Upload Server", "--group", "--disabled-
password", "cstatic-upload"]  
VOLUME ["/etc/ceph", "/secrets"]  
USER cstatic-upload  
ENTRYPOINT ["/go/bin/upload_server"]  

