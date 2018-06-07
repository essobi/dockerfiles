FROM alpine:3.3  
  
COPY . /go/src/github.com/wowgroup/kinesink  
RUN apk -Uv add go git \  
&& cd /go/src/github.com/wowgroup/kinesink \  
&& export GOPATH=/go \  
&& go get \  
&& go build -o /usr/bin/kinesink \  
&& apk del --purge go git \  
&& rm -rf /go /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/kinesink"]  

