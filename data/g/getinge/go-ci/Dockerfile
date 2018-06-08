FROM golang:1.9  
RUN go get -u github.com/mitchellh/gox github.com/stretchr/testify/...
github.com/kardianos/govendor github.com/kisielk/errcheck
github.com/golang/lint/golint github.com/go-swagger/go-swagger/cmd/swagger
github.com/jteeuwen/go-bindata/... github.com/elazarl/go-bindata-assetfs/...
golang.org/x/tools/cmd/goimports github.com/gogo/protobuf/protoc-gen-gogo  
RUN export PATH=$PATH:$GOPATH/bin  
RUN apt-get update -y && apt-get install unzip -y  
RUN wget
https://github.com/google/protobuf/releases/download/v3.1.0/protoc-3.1.0-linux-x86_64.zip  
RUN unzip protoc-3.1.0-linux-x86_64.zip  
RUN export PATH=$PATH:$(pwd)/bin  
COPY *.sh /root/  

