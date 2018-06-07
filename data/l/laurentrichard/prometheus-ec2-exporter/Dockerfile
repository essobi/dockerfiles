FROM golang:1.9.1-alpine as builder  
MAINTAINER easylo <easylo@users.noreply.github.com>  
  
ENV PATH /go/bin:/usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV CGO_ENABLED=0  
COPY . $GOPATH/src/github.com/easylo/prometheus-ec2-exporter  
WORKDIR $GOPATH/src/github.com/easylo/prometheus-ec2-exporter  
  
RUN apk add --update --no-cache \  
make \  
git \  
ca-certificates  
  
# RUN make install  
# RUN go get -u github.com/aws/aws-sdk-go  
RUN make build  
  
FROM quay.io/prometheus/busybox:latest  
COPY \--from=builder /go/src/github.com/easylo/prometheus-
ec2-exporter/prometheus-ec2-exporter /bin/prometheus-ec2-exporter  
ENTRYPOINT ["/bin/prometheus-ec2-exporter"]  
EXPOSE 9599  

