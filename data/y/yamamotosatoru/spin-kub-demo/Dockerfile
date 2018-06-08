FROM golang AS build  
  
ADD . /go/src/github.com/lwander/k8s-demo  
  
RUN CGO_ENABLED=0 go install github.com/lwander/k8s-demo  
  
FROM busybox  
COPY \--from=build /go/bin/k8s-demo /k8s-demo  
ADD ./content /content  
  
CMD ["/k8s-demo"]  

