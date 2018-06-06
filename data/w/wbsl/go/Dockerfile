FROM golang:1.9.1-alpine3.6  
ENV GOBINARIES /go/bin  
WORKDIR $GOBINARIES  
RUN apk add --update tini curl gcc musl-dev git && rm -rf /var/cache/apk/* &&\  
echo 'hosts: files [NOTFOUND=return] dns' >> /etc/nsswitch.conf  
RUN ["go","get","github.com/cespare/reflex"]  

