FROM golang  
  
ADD . /go/src/github.com/samanthakem/go-k8s-gke/server  
  
RUN go install github.com/samanthakem/go-k8s-gke/server  
  
ENTRYPOINT /go/bin/server  
  
EXPOSE 8080  

