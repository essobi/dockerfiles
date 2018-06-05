FROM alpine:edge  
  
ENV GOPATH=/go  
  
RUN apk update \  
&& apk add -t build ca-certificates subversion go musl-dev upx \  
&& svn checkout \  
https://github.com/patch-notes/bamba/trunk/containers/bamba-core \  
/go/src/github.com/patch-notes/bamba/containers/bamba-core \  
&& go build -ldflags="-s -w" github.com/patch-notes/bamba/containers/bamba-
core/ \  
&& upx \--brute bamba-core \  
&& apk del build \  
&& rm -rf /go /var/cache  
  
ENTRYPOINT ["/bamba-core"]  

