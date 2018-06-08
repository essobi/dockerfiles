# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/jimmason/snippy  
  
# Build the snippy inside the container.  
RUN go install github.com/jimmason/snippy/src/snippy  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/bin/snippy  
  
# http server listens on port 8080.  
EXPOSE 8080  

