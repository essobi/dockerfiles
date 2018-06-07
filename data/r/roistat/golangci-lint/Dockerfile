FROM golang  
  
RUN go get -u github.com/golangci/golangci-lint/cmd/golangci-lint  
  
ADD config.yaml /go/src/.golangci.yaml  
  
WORKDIR /go/src  
  
ENTRYPOINT [ "golangci-lint", "run" ]  

