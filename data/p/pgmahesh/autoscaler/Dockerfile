# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang  
  
# Copy the local package files to the container's workspace.  
ADD . /go  
RUN ls -l /go  
  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN go get github.com/gin-gonic/gin  
RUN go get github.com/coopernurse/gorp  
RUN go get github.com/samuel/go-zookeeper/zk  
RUN go get -u github.com/aws/aws-sdk-go  
RUN go get github.com/go-ini/ini  
RUN go get github.com/jmespath/go-jmespath  
RUN go get k8s.io/kubernetes/pkg/api  
RUN go get github.com/pivotal-golang/bytefmt  
RUN go get github.com/aws/aws-sdk-go/service/apigateway  
  
RUN go build /go/src/services/autoscaler.go  
RUN ls -l  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT /go/autoscaler > dis.log  
  
# Document that the service listens on port 8000.  
EXPOSE 9000

