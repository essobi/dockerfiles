FROM alpine:edge  
ENTRYPOINT ["/docker-start"]  
  
COPY . /go/src/github.com/42wim/matterbridge  
COPY matterbridge.toml.in /matterbridge.toml.in  
COPY docker-start /docker-start  
  
RUN apk update && apk add go git gcc m4 musl-dev ca-certificates \  
&& cd /go/src/github.com/42wim/matterbridge \  
&& export GOPATH=/go \  
&& go get \  
&& go build -x -ldflags "-X main.githash=$(git log --pretty=format:'%h' -n 1)"
-o /bin/matterbridge \  
&& rm -rf /go \  
&& apk del --purge git go gcc musl-dev  

