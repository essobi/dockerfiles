FROM golang:1.6.2-alpine  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/vinaykp/linktx  
  
RUN go install github.com/vinaykp/linktx  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/bin/linktx  
  
EXPOSE 8080  

