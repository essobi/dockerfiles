# build stage  
FROM golang:alpine AS build-env  
RUN apk add --update curl git && rm -rf /var/cache/apk/*  
WORKDIR /go/src/github.com/golang/openbaton/go-docker-driver  
RUN export GOPATH=/go  
COPY . .  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 &&
chmod +x /usr/local/bin/dep  
RUN dep ensure -v  
WORKDIR /go/src/github.com/golang/openbaton/go-docker-driver/main  
RUN go build -o goapp  
  
# final stage  
FROM alpine  
WORKDIR /app  
COPY \--from=build-env /go/src/github.com/golang/openbaton/go-docker-
driver/main/goapp /app/  
ENTRYPOINT ["./goapp"]  

