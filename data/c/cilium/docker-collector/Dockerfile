FROM golang:1.5  
MAINTAINER "André Martins <aanm90@gmail.com>"  
COPY . /go/src/github.com/cilium-team/docker-collector  
WORKDIR /go/src/github.com/cilium-team/docker-collector  
ENV GOBIN /go/bin  
  
RUN GOPATH=/go/src/github.com/cilium-team/docker-collector/Godeps/_workspace:\  
/go:$GOPATH \  
CGO_ENABLED=0 go install -v -a docker-collector.go containersregistry.go && \  
mkdir -p /docker-collector/configs && \  
mv /go/src/github.com/cilium-team/docker-collector/configs /docker-collector
&& \  
rm -fr /go/src  
  
WORKDIR /go/bin  
  
ENTRYPOINT ["/go/bin/docker-collector"]  

