FROM golang:alpine as consul-builder  
RUN apk update  
RUN apk add git gcc musl-dev upx  
RUN go get --ldflags='-w -s' github.com/hashicorp/consul  
RUN upx bin/consul  
  
FROM alpine:latest as dumb-init-builder  
RUN apk update  
RUN apk add git make bash gcc musl-dev  
WORKDIR /build  
RUN git clone https://github.com/Yelp/dumb-init.git  
WORKDIR /build/dumb-init  
RUN make  
  
FROM alpine:latest  
RUN apk --no-cache update && apk --no-cache add ca-certificates  
COPY \--from=consul-builder /go/bin/consul /usr/local/bin/  
COPY \--from=dumb-init-builder /build/dumb-init/dumb-init /usr/local/bin  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/usr/local/bin/consul"]  
  
EXPOSE 8300/tcp 8301/tcp 8301/udp 8302/tcp 8302/udp 8500/tcp 8600/tcp 8600/udp  
  
VOLUME /consul/config  
VOLUME /consul/data  
  
COPY config /consul/config  
  
CMD ["agent", "-ui", "-config-dir=/consul/config"]  

