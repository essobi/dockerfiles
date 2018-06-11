FROM golang:1.6.2-alpine  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
RUN set -x && apk add --no-cache --virtual .build_deps git make  
RUN go get github.com/tools/godep  
  
ADD . $GOPATH/src/github.com/yamamoto-febc/arukas-ship  
WORKDIR $GOPATH/src/github.com/yamamoto-febc/arukas-ship  
RUN make build  
  
ENTRYPOINT ["bin/arukas-ship"]  
  

