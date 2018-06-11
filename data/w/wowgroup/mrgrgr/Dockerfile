FROM alpine:3.4  
MAINTAINER WOW! Group Development  
  
COPY . /go/src/github.com/wowgroup/mrgrgr  
RUN apk -Uv add git go ca-certificates \  
&& cd /go/src/github.com/wowgroup/mrgrgr \  
&& export GOPATH=/go \  
&& go build -o /bin/mrgrgr \  
&& apk --purge -v del git go \  
&& rm -rf /go /var/cache/apk/*  
  
ENTRYPOINT ["/bin/mrgrgr"]  

