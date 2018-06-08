FROM debian:jessie  
  
RUN apt-get update -q && apt-get install -qy curl build-essential golang git
linux-libc-dev  
  
ENV GOPATH /go  
  
WORKDIR /go/src/github.com/coreos/flannel  
  
ADD . /go/src/github.com/coreos/flannel/  
  
RUN go build -o ${GOPATH}/bin/flanneld .  
  
CMD ["./installer"]  

