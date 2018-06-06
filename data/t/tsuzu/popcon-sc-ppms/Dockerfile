FROM golang:1.8  
MAINTAINER Tsuzu  
  
RUN mkdir -p $GOPATH/src/github.com/cs3238-tsuzu/ && cd
$GOPATH/src/github.com/cs3238-tsuzu/ && git clone -b swarm
https://github.com/cs3238-tsuzu/popcon-sc  
RUN mkdir -p $GOPATH/src/github.com/cs3238-tsuzu/popcon-sc/ppms  
COPY ./ $GOPATH/src/github.com/cs3238-tsuzu/popcon-sc/ppms  
RUN go get -v github.com/cs3238-tsuzu/popcon-sc/ppms  
  
WORKDIR $GOPATH/src/github.com/cs3238-tsuzu/popcon-sc/ppms  
ENTRYPOINT ["ppms"]  

