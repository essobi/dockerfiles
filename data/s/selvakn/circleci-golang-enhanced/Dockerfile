FROM circleci/golang:1.9  
# Install dep  
RUN curl -sL https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-
amd64 > /go/bin/dep  
RUN chmod +x /go/bin/dep  
  
# Install go-bindata  
RUN go get -u github.com/jteeuwen/go-bindata/...  

