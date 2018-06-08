FROM ubuntu:14.04.1  
MAINTAINER ontouchstart <ontouchstart@gmail.com>  
  
RUN apt-get update -qq -y  
RUN apt-get install gcc libc6-dev git bzr -y  
  
RUN git clone https://go.googlesource.com/go && cd go && git checkout go1.4.1  
RUN cd go/src && ./all.bash  
RUN /go/bin/go version  
  
ENV GOARCH amd64  
ENV GOOS linux  
ENV GOROOT /go  
ENV GOBIN $GOROOT/bin  
ENV PATH $GOBIN:$PATH  
ENV GOPATH /  
  
ENV HOME /home  
WORKDIR /home  

