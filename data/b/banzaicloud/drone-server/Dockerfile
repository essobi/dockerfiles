# docker build --rm -t banzaicloud/drone .  
FROM golang:1.9 as golang  
ADD . /go/src/github.com/drone/drone  
WORKDIR /go/src/github.com/drone/drone  
  
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/drone-server
github.com/drone/drone/cmd/drone-server  
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/drone-agent
github.com/drone/drone/cmd/drone-agent  
  
FROM alpine:3.6 as alpine  
RUN apk add \--no-cache ca-certificates  
  
FROM alpine:3.6  
EXPOSE 8000 9000 80 443  
  
ENV DATABASE_DRIVER=sqlite3  
ENV DATABASE_CONFIG=/var/lib/drone/drone.sqlite  
ENV GODEBUG=netdns=go  
ENV XDG_CACHE_HOME /var/lib/drone  
  
COPY \--from=golang /release/drone-server /bin  
COPY \--from=golang /release/drone-agent /bin  
COPY \--from=alpine /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/  
  
ENTRYPOINT ["/bin/drone-server"]  

