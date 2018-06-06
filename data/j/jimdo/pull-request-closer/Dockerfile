FROM golang:1.5.3  
WORKDIR /go/src/github.com/Jimdo/pull-request-closer  
Add . /go/src/github.com/Jimdo/pull-request-closer  
  
# Get godeps from main repo  
RUN go get github.com/tools/godep  
  
RUN go get golang.org/x/sys/unix  
  
# Restore godep dependencies  
RUN godep restore  
  
# Install  
RUN go install github.com/Jimdo/pull-request-closer  
  
ENTRYPOINT ["/go/bin/pull-request-closer"]  

