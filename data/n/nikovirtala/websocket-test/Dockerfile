FROM golang:alpine as build  
  
ADD . /root/  
WORKDIR /root  
RUN apk add --no-cache git && go get github.com/gorilla/websocket  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o websockets .  
  
FROM alpine:edge  
LABEL maintainer "Niko Virtala <niko@nikovirtala.io>"  
  
WORKDIR /  
COPY \--from=build /root/websockets .  
COPY \--from=build /root/websockets.html .  
EXPOSE 80  
ENTRYPOINT ["/websockets"]  

