# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang:1.5.1  
# Copy the local package files to the container's workspace.  
ADD . /go/src/github.com/cj123/canijailbreak.com  
  
# Build the outyet command inside the container.  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN cd /go/src/github.com/cj123/canijailbreak.com && go get . && go build .  
  
EXPOSE 9062  
# Run the outyet command by default when the container starts.  
ENTRYPOINT cd /go/src/github.com/cj123/canijailbreak.com \  
&& /go/src/github.com/cj123/canijailbreak.com/canijailbreak.com  
  

