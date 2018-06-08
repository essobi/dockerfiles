FROM golang  
  
RUN go get github.com/yuuichi-fujioka/k8sfs/cmd/k8sfs  
  
FROM ubuntu:xenial  
LABEL maintainer="fujioka.yuuichi@gmail.com"  
  
RUN apt-get update && apt-get install fuse -y && apt-get clean  
  
COPY \--from=0 /go/bin/k8sfs .  
  
ENTRYPOINT ["/k8sfs", "/mnt"]  

