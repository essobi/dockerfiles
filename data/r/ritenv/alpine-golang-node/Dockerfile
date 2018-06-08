FROM gliderlabs/alpine:3.3  
MAINTAINER Riten Vagadiya <i@ritenv.com> (@ritenv)  
RUN echo 'Welcome to Alpine, all set for Golang and Node!'  
RUN apk update && apk add curl git go && mkdir /gopath  
  
RUN apk add nodejs  
RUN apk add go  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /gopath  
ENV GOBIN /gopath/bin  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
RUN go get github.com/gorilla/mux  
RUN go get gopkg.in/mgo.v2

