FROM golang AS builder  
RUN apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install libvirt-dev  
WORKDIR /go/src/github.com/zobees/gse  
COPY . .  
RUN go get -d -v ./cmd/... && \  
go install -v ./cmd/...  
  
FROM debian:jessie  
MAINTAINER Cliff Rowley <cliffrowley@gmail.com>  
RUN apt-get -y update && apt-get -y install ca-certificates && rm -rf
/var/lib/apt/lists/*  
ENV PATH="$PATH:/gse/bin"  
RUN mkdir -p /gse/bin  
WORKDIR /gse  
COPY \--from=builder /go/bin ./bin/  
COPY run.sh ./bin/  
RUN chmod +x ./bin/*  
CMD run.sh

