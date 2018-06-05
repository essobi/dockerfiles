# FROM golang:1.9.4-alpine3.6  
FROM golang:1.10.2-alpine3.7 as builder  
  
RUN apk add --update git && \  
go get -d github.com/devcodewak/avonsg_openshift/cmd && \  
go build -ldflags="-s -w" -o /go/bin/web
github.com/devcodewak/avonsg_openshift/cmd  
  
FROM alpine:3.7  
WORKDIR /bin/  
  
COPY \--from=builder /go/bin/web .  
  
RUN web -version  
  
CMD ["/bin/web", "-server", "-cmd", "-key",
"809240d3a021449f6e67aa73221d42df942a308a", "-listen", "http2://:8443",
"-listen", "http://:8444", "-log", "null"]  
  
EXPOSE 8443 8444

