FROM golang:1.8 as build  
  
ARG PROTOC_VER=3.3.0  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install unzip && \  
apt-get clean  
  
ADD
https://github.com/google/protobuf/releases/download/v${PROTOC_VER}/protoc-${PROTOC_VER}-linux-x86_64.zip
/tmp/protoc.zip  
RUN mkdir -p /opt/protoc && \  
cd /opt/protoc && \  
unzip /tmp/protoc.zip && \  
rm -f /tmp/protoc.zip && \  
ln -s /opt/protoc/bin/* /usr/bin  
  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
  
WORKDIR /go/src/github.com/influxdata/telegraf  
  
COPY . .  
  
RUN make prepare build build-for-docker  
  
FROM golang:1.8 as app  
  
WORKDIR /app  
COPY \--from=build /go/bin/telegraf /app  
COPY etc /etc/telegraf  
  
ENTRYPOINT ["/app/telegraf"]

