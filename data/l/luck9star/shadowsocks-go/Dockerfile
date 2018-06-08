FROM golang:alpine  
RUN echo $(go version)  
RUN apk --update add git \  
&& rm -rf /var/cache/apk/*  
# RUN apk-install git  
RUN go get github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-server && rm
-rf /go/pkg /go/src  
ENTRYPOINT ["shadowsocks-server"]  

