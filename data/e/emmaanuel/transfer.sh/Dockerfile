FROM golang:1.7  
MAINTAINER Emmaanuel  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/emmaanuel/transfer.sh  
  
# build & install server  
RUN go build -o /go/bin/transfersh github.com/emmaanuel/transfer.sh  
  
CMD ["/go/bin/transfersh", "--listener", ":8080", "--provider", "local", "--
basedir", "/tmp"]  
  
EXPOSE 8080  

