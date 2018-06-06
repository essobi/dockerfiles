FROM golang:1.7-alpine  
  
ENTRYPOINT ["/bin/chopped"]  
  
COPY . /go/src/github.com/pieoneers/chopped  
  
RUN set -ex \  
&& apk add \--no-cache --virtual .build-deps \  
git \  
mercurial \  
&& cd /go/src/github.com/pieoneers/chopped \  
&& export GOPATH=/go \  
&& go get \  
&& go build -o /bin/chopped \  
&& rm -rf /go \  
&& apk del .build-deps  

