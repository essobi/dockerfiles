FROM alpine  
  
MAINTAINER G@gmail.com  
  
RUN apk add --no-cache --virtual=.build-dependencies go gcc git libc-dev ca-
certificates \  
&& export GOPATH=/tmp/go \  
&& git clone https://github.com/ginuerzh/gost
$GOPATH/src/github.com/ginuerzh/gost \  
&& cd $GOPATH/src/github.com/ginuerzh/gost/cmd/gost \  
&& go build \  
&& mv $GOPATH/src/github.com/ginuerzh/gost/cmd/gost/gost /usr/local/bin/lost \  
&& apk del .build-dependencies \  
&& rm -rf /tmp  
  
EXPOSE 80 8080 8088  
  
ENTRYPOINT ["/usr/local/bin/lost"]  

