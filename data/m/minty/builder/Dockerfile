# Docker Image Builder  
#  
# Create builder binary  
FROM dockercore/docker as builder  
COPY . /go/src/github.com/juztin/builder  
WORKDIR /go/src/github.com/juztin/builder  
ENV CGO_ENABLED=0  
RUN go get && go build  
  
# Create builder image  
FROM alpine  
MAINTAINER Justin Wilson <justin@minty.io>  
COPY \--from=builder /go/src/github.com/juztin/builder/builder /bin/  
ENTRYPOINT ["/bin/builder"]  

