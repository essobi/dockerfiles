FROM golang:alpine  
  
ADD entrypoint.sh /entrypoint.sh  
  
ADD config.yaml /etc/webdav/config.yaml  
  
RUN apk add --no-cache bash git && mkdir /davroot && chmod +x /entrypoint.sh  
  
RUN go get -d github.com/hacdias/webdav/cmd/webdav # && go get
gopkg.in/yaml.v2  
  
RUN go install github.com/hacdias/webdav/cmd/webdav  
  
EXPOSE 8082  
ENTRYPOINT /entrypoint.sh  
  

