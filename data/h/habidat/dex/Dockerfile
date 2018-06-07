FROM golang:alpine  
MAINTAINER Florian Humer <florian.humer@gmail.com>  
  
RUN apk update && apk add curl build-base git mercurial bzr && rm -rf
/var/cache/apk/*  
  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
ENV DEX_HOME $GOPATH/src/github.com/coreos/dex  
  
RUN mkdir -p $DEX_HOME  
  
RUN git clone https://github.com/coreos/dex.git $DEX_HOME  
  
RUN cd $DEX_HOME && \  
make  
  
RUN mkdir /var/config  
RUN mkdir /var/data  
  
VOLUME /var/config  
VOLUME /var/data  
  
CMD $DEX_HOME/bin/dex serve /var/config/config.yaml  
  
WORKDIR $DEX_HOME  
  
EXPOSE 5556  

