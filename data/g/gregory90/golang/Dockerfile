FROM gregory90/base:latest  
  
ENV GO_VERSION 1.10  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
build-essential ca-certificates git mercurial bzr  
RUN mkdir /goroot && curl
https://storage.googleapis.com/golang/go$GO_VERSION.linux-amd64.tar.gz | tar
xvzf - -C /goroot --strip-components=1  
RUN mkdir /gopath  
  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  

