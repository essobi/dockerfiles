FROM golang:1.10 AS build-containerd  
RUN apt-get update -q && apt-get install -yq libseccomp-dev  
WORKDIR /go/src/github.com/containerd/containerd  
COPY . /go/src/github.com/containerd/containerd  
RUN BUILDTAGS='seccomp apparmor no_btrfs no_cri' make  
  
FROM debian:stretch AS build-criu  
RUN apt-get update -q && apt-get install -yq --no-install-recommends curl
build-essential libprotobuf-dev \  
libprotobuf-c0-dev protobuf-c-compiler protobuf-compiler python-protobuf
libnl-3-dev pkg-config python-ipaddr \  
iproute2 libcap-dev libnet1-dev ca-certificates git asciidoc xmlto  
ARG CRIU_VERSION=3.8.1  
RUN curl -sSL https://github.com/checkpoint-
restore/criu/archive/v${CRIU_VERSION}.tar.gz | tar xzv --strip-components=1 -C
/tmp  
RUN cd /tmp && make && make install  
  
FROM fermayo/runc:latest-debian  
RUN apt-get update -q && apt-get install -yq libseccomp2 ca-certificates
libprotobuf-c1 libnl-3-200 iproute2 libcap2 libnet1 iptables  
VOLUME /var/lib  
COPY \--from=build-criu /usr/local/sbin/criu /usr/local/sbin/  
COPY \--from=build-containerd /go/src/github.com/containerd/containerd/bin/*
/usr/local/bin/  
CMD ["ctr"]  

