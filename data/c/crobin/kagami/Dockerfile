FROM golang:1.8 AS build  
  
ENV CGO_ENABLED=0  
COPY . /go/src/github.com/christopherobin/kagami  
  
WORKDIR /go/src/github.com/christopherobin/kagami  
RUN make tools deps install  
WORKDIR /  
  
FROM scratch  
  
COPY \--from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
COPY \--from=build /go/bin/kagami /  
  
ENTRYPOINT ["/kagami"]  

