# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
# Build the outyet command inside the container.  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN go get github.com/maxmcd/kayobe  
RUN go install github.com/maxmcd/kayobe  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/bin/kayobe  
  
# Document that the service listens on port 8000.  
EXPOSE 8000

