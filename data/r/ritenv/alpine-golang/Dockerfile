FROM gliderlabs/alpine:3.3  
MAINTAINER Riten Vagadiya <i@ritenv.com> (@ritenv)  
RUN echo 'Welcome to Alpine, all set for Golang!'  
RUN apk update && apk add curl git go && mkdir /gopath  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /gopath  
ENV GOBIN /gopath/bin  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  

