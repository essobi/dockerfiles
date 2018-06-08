FROM ubuntu:14.04  
  
ENV PKG github.com/mattn/goreman  
ENV GOPATH /usr/local/go  
ENV GOBIN $GOPATH/bin  
ENV PATH $GOBIN:$PATH  
RUN apt-get -qy update && apt-get -qy install golang-go git mercurial && apt-
get -qy clean  
ADD . $GOPATH/src/$PKG  
RUN go get -v $PKG  

