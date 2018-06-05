FROM golang:1.9  
ADD . /go/src/github.com/mulesoft-ops/hello-world-k8s  
WORKDIR /go/src/github.com/mulesoft-ops/hello-world-k8s  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /hello-
world-k8s .  
  
FROM alpine  
COPY \--from=0 /hello-world-k8s /hello-world-k8s  
ADD ./content /content  
ENTRYPOINT /hello-world-k8s  

