FROM golang:1.6.2-wheezy  
MAINTAINER Fabian Stäber, fabian@fstab.de  
  
ENV LAST_UPDATE=2016-05-08  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y \  
build-essential  
  
RUN go get github.com/mitchellh/gox  
# Need to move gox out of $GOPATH, because $GOPATH will be replaced with the
volume on the host system.  
RUN mv $GOPATH/bin/gox /usr/bin  

