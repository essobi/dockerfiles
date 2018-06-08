FROM google/golang  
  
WORKDIR /gopath/src/github.com/flyinprogrammer/ec2metaproxy  
ADD . /gopath/src/github.com/flyinprogrammer/ec2metaproxy  
RUN go get github.com/flyinprogrammer/ec2metaproxy/cmd/ec2metaproxy  
  
CMD []  
ENTRYPOINT ["/gopath/bin/ec2metaproxy"]

