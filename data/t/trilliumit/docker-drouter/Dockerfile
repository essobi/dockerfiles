FROM golang:1.8  
MAINTAINER Trillium IT <webmaster@trilliumit.com>  
  
ENV GO15VENDOREXPERIMENT 1  
RUN go get github.com/Masterminds/glide  
  
ENV SRC_ROOT /go/src/github.com/TrilliumIT/docker-drouter  
  
# Setup our directory and give convenient path via ln.  
RUN mkdir -p ${SRC_ROOT}  
  
WORKDIR ${SRC_ROOT}  
  
# Used to only go get if sources change.  
ADD glide.* ${SRC_ROOT}/  
RUN $GOPATH/bin/glide install  
  
ADD . ${SRC_ROOT}/  
RUN go get $($GOPATH/bin/glide novendor)  
  
ENTRYPOINT ["/go/bin/docker-drouter"]  

