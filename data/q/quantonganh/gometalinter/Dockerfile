FROM golang:alpine  
  
RUN apk add \--no-cache gcc git musl-dev  
  
RUN go get -u github.com/alecthomas/gometalinter && \  
gometalinter --install && \  
mv /go/bin/* /usr/local/bin/ && \  
rm -fr /go/pkg /go/*/*  

