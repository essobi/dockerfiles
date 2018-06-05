From ubuntu:14.04  
MAINTAINER bowwow <bowwow@gmail.com>  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
build-essential ca-certificates git mercurial bzr  
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.6.linux-
amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1  
RUN mkdir /gopath  
RUN mkdir /go  
  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
EXPOSE 8888 8443  
ONBUILD COPY bin/goapi /go/  
VOLUME ["/go"]  
WORKDIR /go  
  
CMD ["./goapi"]  

