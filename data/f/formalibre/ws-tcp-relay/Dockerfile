FROM golang:1.7-alpine3.5  
RUN apk add \--no-cache --virtual .persistent-deps \  
git  
RUN go get -u github.com/joshglendenning/ws-tcp-relay  
EXPOSE 4223  

