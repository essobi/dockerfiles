FROM golang:1.7.3-alpine  
RUN apk add --no-cache git gcc musl-dev tzdata && go get github.com/beego/bee
&& rm -rf /go/src/* && rm -rf /go/pkg/*  
RUN go get github.com/smartystreets/goconvey  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  

