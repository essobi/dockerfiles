FROM docker.io/centos:7  
MAINTAINER Dan Burke <dburke@liquidweb.com>  
  
RUN yum clean all && yum update -y && yum clean all  
RUN yum install golang git -y && yum clean all  
  
ENV GOPATH /root/go  
  
ADD . /tpw/  
  
RUN go get github.com/coreos/go-etcd/etcd  
RUN go get github.com/fsouza/go-dockerclient  
RUN cd /tpw && go build third-party-watcher.go  
  
CMD ["/tpw/third-party-watcher"]  
  

