# GoPlay, A Tour of Go  
# VERSION 0.1  
# DOCKER-VERSION 0.4.8  
FROM ubuntu:12.04  
MAINTAINER Victor Vieux <victor@vvieux.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install mercurial build-essential -y  
RUN hg clone -u release https://code.google.com/p/go  
RUN cd go/src && ./make.bash  
RUN ln -s /go/bin/go /bin/go  
  
EXPOSE 3999  
CMD go run go/misc/goplay/goplay.go -http="0.0.0.0:3999"

