# OR: "onbuild" makes it even easier:  
# FROM golang:onbuild  
# EXPOSE 8080  
# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/witekcc/git-mass-pull  
  
# Build the git-mass-pull command inside the container.  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN go install github.com/witekcc/git-mass-pull  
  
# Run the git-mass-pull command by default when the container starts.  
ENTRYPOINT /go/bin/git-mass-pull  
  
# Document that the service listens on port 8080.  
EXPOSE 8080  

