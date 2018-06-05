FROM arken/gom-base  
MAINTAINER Damien Metzler <dmetzler@nuxeo.com>  
  
RUN go get github.com/arkenio/etcd-netfw  
WORKDIR /usr/local/go/src/github.com/arkenio/etcd-netfw  
RUN gom install  
RUN gom test  
RUN gom build  
  
# Expose default listening amb port  
EXPOSE 1337  
ENTRYPOINT ["/usr/local/go/src/github.com/arkenio/etcd-netfw/etcd-netfw",
"-etcdAddress", "http://172.17.42.1:4001"]  

