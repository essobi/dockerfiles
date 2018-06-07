FROM golang:1.10 AS build-runc  
RUN apt-get update -q && apt-get install -yq btrfs-tools libseccomp-dev  
WORKDIR /go/src/github.com/opencontainers/runc  
COPY . /go/src/github.com/opencontainers/runc  
RUN make runc  
  
FROM debian:stretch  
RUN apt-get update -q && apt-get install -yq libseccomp2  
COPY \--from=build-runc /go/src/github.com/opencontainers/runc/runc
/usr/local/bin/runc  
CMD ["runc"]  

