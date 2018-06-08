FROM golang:1.5.2  
  
RUN go get github.com/laher/goxc github.com/tools/godep  
  
ENV GOROOT_BOOTSTRAP=/usr/local/go  
  
RUN goxc -t  

