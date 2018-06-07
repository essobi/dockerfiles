# Useful Dockerfile with Go and Emboxen Framework.  
# This also includes an example building environment called "echo".  
FROM debian:jessie  
MAINTAINER Tomoaki KAWADA <i@yvt.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -y dist-upgrade \  
&& apt-get -y install \  
golang ca-certificates mercurial git subversion nano apt-transport-https \  
g++ \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOPATH /go  
WORKDIR $GOPATH  
  
ADD . /go/src/github.com/yvt/emboxen-framework  
RUN go get github.com/yvt/emboxen-framework \  
&& go install github.com/yvt/emboxen-framework github.com/yvt/emboxen-
framework/echo  
  
CMD /go/bin/echo  
  

