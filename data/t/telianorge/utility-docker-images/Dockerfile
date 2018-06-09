FROM alpine/git:latest as jsonnet-cloner  
ENV GOPATH /go  
RUN git clone https://github.com/google/go-jsonnet.git
$GOPATH/src/github.com/google/go-jsonnet  
RUN cd $GOPATH/src/github.com/google/go-jsonnet && git checkout v0.10.0  
  
FROM golang:1.10 as builder  
ENV GOPATH /go  
RUN go get github.com/fatih/color  
COPY \--from=jsonnet-cloner $GOPATH/src/github.com/google/go-jsonnet
$GOPATH/src/github.com/google/go-jsonnet  
WORKDIR $GOPATH/src/github.com/google/go-jsonnet  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /jsonnet-amd64 -v
jsonnet/cmd.go  
  
FROM alpine/git:latest as remarshal-cloner  
RUN git clone https://github.com/dbohdan/remarshal.git /src/remarshal  
RUN cd /src/remarshal && git checkout v0.8.0  
  
FROM python:3.6-alpine3.7 as resource  
COPY \--from=builder /jsonnet-amd64 /usr/local/bin/jsonnet  
COPY \--from=remarshal-cloner /src/remarshal /src/remarshal  
RUN apk add --update make  
RUN chmod +x /usr/local/bin/jsonnet  
WORKDIR /src/remarshal  
RUN python setup.py install  
  
FROM resource  

