FROM builtdock/base:latest  
MAINTAINER BuiltDock Project <info@builtdock.com>  
  
# install go runtime  
RUN wget -qO- https://storage.googleapis.com/golang/go1.3.1.linux-amd64.tar.gz
| tar -C /usr/local -xz  
  
# prepare go environment  
RUN mkdir -p /go  
ENV GOPATH /go  
ENV PATH /usr/local/bin:/usr/bin:/bin:/sbin:/usr/local/go/bin  
  
# create /var/log/builtdock for holding logs (access via bind mount)  
RUN mkdir -p /var/log/builtdock  
  
# prepare execution environment  
WORKDIR /app  
CMD ["/app/bin/boot"]  
EXPOSE 514  
ADD . /app  
ADD . /go/src/github.com/builtdock/builtdock/logger  
  
# compile the binary  
RUN cd /go/src/github.com/builtdock/builtdock/logger/syslogd && go install -v
.  

