# docker build --rm -t banzaicloud/drone .  
FROM golang:1.9 as golang  
ADD . /go/src/github.com/drone/drone  
WORKDIR /go/src/github.com/drone/drone  
  
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /release/drone-agent
github.com/drone/drone/cmd/drone-agent  
  
FROM alpine:3.6 as alpine  
RUN apk add --no-cache ca-certificates  
  
FROM alpine:3.6  
EXPOSE 3000  
ENV GODEBUG=netdns=go  
  
COPY \--from=golang /release/drone-agent /bin  
COPY \--from=alpine /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/  
  
HEALTHCHECK CMD ["/bin/drone-agent", "ping"]  
  
ENTRYPOINT ["/bin/drone-agent"]  

