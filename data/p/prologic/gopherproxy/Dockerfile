FROM golang:alpine  
  
EXPOSE 80/tcp  
  
ENTRYPOINT ["gopherproxy"]  
  
RUN \  
apk add --update git && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /go/src/github.com/prologic/gopherproxy  
WORKDIR /go/src/github.com/prologic/gopherproxy  
  
COPY . /go/src/github.com/prologic/gopherproxy  
  
RUN go get -v -d  
RUN go install -v github.com/prologic/gopherproxy/...  

