FROM golang:1.9 as builder  
  
WORKDIR $GOPATH/src  
  
RUN go get -t github.com/urfave/cli && \  
go get -t github.com/visionmedia/go-debug && \  
go get -t github.com/kelseyhightower/envconfig && \  
go get -t github.com/denverdino/aliyungo/oss && \  
go get -t github.com/codeskyblue/go-sh && \  
mkdir web-app-tool  
  
ADD web-app-tool.go ./web-app-tool  
ADD src ./web-app-tool/src  
  
WORKDIR $GOPATH/src/web-app-tool  
  
RUN go build --ldflags '-linkmode external -extldflags "-static"' web-app-
tool.go  
  
FROM node:alpine  
  
WORKDIR /root/  
  
COPY \--from=builder /go/src/web-app-tool/web-app-tool .  
  
CMD ["./web-app-tool"]  
  

