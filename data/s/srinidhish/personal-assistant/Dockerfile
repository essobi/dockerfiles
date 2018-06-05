FROM golang  
  
  
  
# I am not able to understand this -- go get downloads and installs but it is
not working so i am installing manually  
RUN go get github.com/jteeuwen/go-bindata  
WORKDIR $GOPATH/src/github.com/jteeuwen/go-bindata/go-bindata  
RUN go install  
  
RUN go get -u github.com/golang/dep/cmd/dep  
WORKDIR $GOPATH/src/github.com/golang/dep/cmd/dep  
RUN go install  
  
ADD . /go/src/github.com/twlabs/personal-assistant  
WORKDIR /go/src/github.com/twlabs/personal-assistant  
RUN dep ensure  
RUN go generate  
  
RUN go install github.com/twlabs/personal-assistant  
  
ENTRYPOINT /go/bin/personal-assistant  
  
EXPOSE 8080  

