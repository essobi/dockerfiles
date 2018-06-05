FROM golang:1.7.1  
RUN mkdir -p "$GOPATH/src/github.com/kuberlab/dealer-clusters-rpc"  
  
COPY . "$GOPATH/src/github.com/kuberlab/dealer-clusters-rpc"  
  
RUN go install -v "github.com/kuberlab/dealer-clusters-rpc"  
  
CMD [ "dealer-clusters-rpc" ]  

