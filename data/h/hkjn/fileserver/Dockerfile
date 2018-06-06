#  
# Minimal service to serve contents from the file system over HTTP.  
#  
FROM golang  
  
MAINTAINER Henrik Jonsson <me@hkjn.me>  
  
# Path inside the container to serve files from. Likely will be  
# bind mounted from host path or another container at runtime.  
ENV FILES_DIR /var/www  
RUN mkdir -p $FILES_DIR  
  
WORKDIR /go/src/hkjn.me/fileserver/  
COPY *.go ./  
RUN go test -race && \  
go vet && \  
go install  
  
ENTRYPOINT ["fileserver"]  

