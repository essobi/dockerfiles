FROM golang:latest  
  
RUN go get github.com/kardianos/govendor  
  
RUN go get -d github.com/dotpy3/apartment-alert  
WORKDIR $GOPATH/src/github.com/dotpy3/apartment-alert  
RUN govendor sync  
  
RUN go build -o /apartment-alert  
RUN chmod +x /apartment-alert  
  
ENTRYPOINT /apartment-alert  

