FROM golang:1.9.0-alpine  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
RUN apk add \--no-cache make git bash parallel gcc musl-dev  
RUN go get github.com/golang/dep/cmd/dep  
RUN go get github.com/golang/lint/golint  

