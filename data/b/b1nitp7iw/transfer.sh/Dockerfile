FROM golang:1.7-alpine  
LABEL maintainer="Remco Verhoef <remco@dutchcoders.io>"  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/dutchcoders/transfer.sh  
  
# build & install server  
RUN go build -o /go/bin/transfersh github.com/dutchcoders/transfer.sh  
  
RUN chmod -R 777 /tmp  
  
USER 1001  
ENTRYPOINT ["/go/bin/transfersh", "--listener", ":8080", "--provider",
"local", "--basedir", "/tmp/"]  
  
EXPOSE 8080 8080  

