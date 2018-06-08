FROM golang:1  
RUN curl -qL
https://github.com/Masterminds/glide/releases/download/v0.13.1/glide-v0.13.1-linux-
amd64.tar.gz | tar xz  
ADD . /go/src/github.com/flix-tech/k8s-mdns  
WORKDIR /go/src/github.com/flix-tech/k8s-mdns  
RUN /go/linux-amd64/glide install  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o k8s-mdns .  
FROM scratch  
COPY \--from=0 /go/src/github.com/flix-tech/k8s-mdns/k8s-mdns /k8s-mdns  
ENTRYPOINT ["/k8s-mdns", "--logtostderr"]  

