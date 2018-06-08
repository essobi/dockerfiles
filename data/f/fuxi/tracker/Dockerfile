# based on http://carlosbecker.com/posts/small-go-apps-containers/  
FROM alpine:3.2  
ENV GOROOT=/usr/lib/go \  
GOPATH=/gopath \  
GOBIN=/gopath/bin \  
PATH=$PATH:$GOROOT/bin:$GOPATH/bin \  
TRACKER_SERVE_ADDRESS=:80  
WORKDIR /gopath/src/github.com/hashtock/tracker  
ADD . /gopath/src/github.com/hashtock/tracker  
  
RUN apk add -U git go && \  
go get github.com/tools/godep && \  
$GOBIN/godep go build -o /usr/bin/tracker && \  
apk del git go && \  
rm -rf /gopath && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 80  
CMD "tracker"  

