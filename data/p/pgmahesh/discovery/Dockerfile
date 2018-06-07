# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go  
RUN ls -l /go  
  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN go get github.com/gin-gonic/gin  
RUN go get github.com/samuel/go-zookeeper/zk  
RUN go get github.com/coopernurse/gorp  
RUN go get k8s.io/kubernetes/pkg/api  
RUN go build /go/src/services/discovery/discovery.go  
RUN ls -l  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/discovery > dis.log  
  
# Document that the service listens on port 8000.  
EXPOSE 8000

