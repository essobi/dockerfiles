FROM golang:1.9-alpine3.7 as build  
  
RUN apk add --no-cache git musl-dev  
RUN go get github.com/golang/dep/cmd/dep  
  
RUN go get github.com/gohugoio/hugo  
WORKDIR /go/src/github.com/gohugoio/hugo  
RUN dep ensure  
RUN go install -ldflags '-s -w'  
  
FROM alpine:3.7  
COPY \--from=build /go/bin/hugo /bin/hugo  
COPY exec.sh /srv/exec.sh  
  
RUN \  
chmod +x /srv/exec.sh && \  
apk add --update --no-cache tzdata curl openssl git ca-certificates && \  
cp /usr/share/zoneinfo/EST /etc/localtime && \  
echo "CDT" > /etc/timezone && date && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /srv/hugo  
CMD ["/srv/exec.sh"]  

