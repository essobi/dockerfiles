FROM golang:1.9 as build  
  
COPY . /go/src/github.com/bitly/oauth2_proxy  
  
WORKDIR /go/src/github.com/bitly/oauth2_proxy  
  
RUN go get ./...  
RUN CGO_ENABLED=0 go build  
  
FROM alpine:3.6  
RUN apk --update add ca-certificates gettext && rm -rf /var/cache/apk/*  
  
COPY \--from=build /go/src/github.com/bitly/oauth2_proxy/oauth2_proxy
/usr/local/bin/  
  
VOLUME /etc/oauth2/  
  
EXPOSE 80  
ENTRYPOINT ["oauth2_proxy", "-config=/etc/oauth2/proxy.cfg"]  

