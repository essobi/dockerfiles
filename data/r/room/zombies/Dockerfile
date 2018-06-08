FROM golang:1.5.1  
  
MAINTAINER Harrison Shoebridge <harrison@theshoebridges.com>  
  
RUN go get github.com/coreos/etcd  
RUN go get github.com/coreos/etcd/client  
RUN go get github.com/coreos/etcd/error  
RUN go get
github.com/coreos/etcd/Godeps/_workspace/src/golang.org/x/net/context  
  
RUN go get github.com/koding/kite  
RUN go get github.com/codegangsta/gin  
RUN go get github.com/bigroom/zombies  
  
RUN go get github.com/paked/configure  
  
RUN go get github.com/bigroom/zombies/cmd/pool  
RUN go get github.com/getsentry/raven-go  
RUN go get github.com/sirupsen/logrus  
  
WORKDIR /go/src/github.com/bigroom/zombies/cmd/pool  
  
CMD gin -i -b "pool"  

