# Container with go toolchain.  
# Create a directory in host and map it to /go volume to persist data between  
# multiple commands.  
# Usage:  
# docker build -t go  
# docker run \--rm -v [dir-in-host]:/go -v $GOPATH/src/app:/go/src/app go get
app  
# docker run \--rm -v [dir-in-host]:/go -v $GOPATH/src/app:/go/src/app go test
app  
# docker run \--rm -v [dir-in-host]:/go -v $GOPATH/src/app:/go/src/app go
build -o app/build/out app  
#  
FROM centos  
MAINTAINER buddyspike <buddyspike@geeksdiary.com> (@buddyspike)  
  
ENV DOWNLOADS /downloads  
ENV TOOLS /tools  
ENV GOROOT $TOOLS/go  
ENV GOPATH /go  
ENV PATH $GOROOT/bin:$PATH  
  
ADD ./setup.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/setup.sh  
RUN setup.sh  
  
ENTRYPOINT ["go"]  
  
WORKDIR $GOPATH/src  

