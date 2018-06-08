FROM golang:alpine  
  
RUN apk add \--update git && \  
git clone -b master https://github.com/ginuerzh/gost/
/go/src/github.com/ginuerzh/gost && \  
cd /go/src/github.com/ginuerzh/gost/cmd/gost && \  
go get ./... && go install github.com/ginuerzh/gost/cmd/gost  
  
ENV PASSWORD=123456 REMOTEADDR=my.serv SNIPROXY=ip.addr MODE=wss  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
  
EXPOSE 8080  

