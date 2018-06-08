FROM golang:1.10-alpine  
  
  
RUN apk update && apk upgrade && apk add bash git make upx  
  
RUN wget -q -O dep https://github.com/golang/dep/releases/download/v0.4.1/dep-
linux-amd64 && \  
echo '31144e465e52ffbc0035248a10ddea61a09bf28b00784fd3fdd9882c8cbb2315 dep' |
sha256sum -c - && \  
mv dep /usr/bin/ && chmod +x /usr/bin/dep  
  
RUN go get -u \  
github.com/golang/lint/golint \  
golang.org/x/tools/cmd/goimports \  
github.com/golang/dep/cmd/dep \  
&& rm -rf $GOPATH/src/* && rm -rf $GOPATH/pkg/*  
  

