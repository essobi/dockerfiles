# build stage  
FROM golang:alpine AS build-env  
RUN apk add --update curl git && rm -rf /var/cache/apk/*  
WORKDIR /go/src/github.com/golang/openbaton/go-docker-vnfm  
RUN export GOPATH=/go  
COPY . .  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 &&
chmod +x /usr/local/bin/dep  
RUN dep ensure -v  
RUN go build -o go-docker-vnfm  
  
# final stage  
FROM alpine  
COPY \--from=build-env /go/src/github.com/golang/openbaton/go-docker-vnfm/go-
docker-vnfm .  
ENTRYPOINT ["./go-docker-vnfm"]  

