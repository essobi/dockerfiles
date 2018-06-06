FROM golang:1.8.1  
RUN mkdir -p "$GOPATH/src/github.com/kuberlab/tensorflow-spawner"  
  
ADD ./pkg "$GOPATH/src/github.com/kuberlab/tensorflow-spawner/pkg"  
ADD ./spawner.go "$GOPATH/src/github.com/kuberlab/tensorflow-
spawner/spawner.go"  
ADD ./vendor "$GOPATH/src/github.com/kuberlab/tensorflow-spawner/vendor"  
  
RUN go install -v "github.com/kuberlab/tensorflow-spawner"  
  
CMD [ "tensorflow-spawner" ]  

