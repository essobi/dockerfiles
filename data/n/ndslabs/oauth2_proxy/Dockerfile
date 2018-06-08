FROM golang:1.7-alpine as build  
RUN apk --update upgrade && apk add git && rm -rf /var/cache/apk/*  
COPY . /go/src/github.com/bitly/oauth2_proxy  
RUN cd /go/src/github.com/bitly/oauth2_proxy && go get && go build  
  
FROM alpine  
RUN apk --update upgrade && apk add ca-certificates && rm -rf /var/cache/apk/*  
COPY \--from=build /go/bin/oauth2_proxy /usr/local/bin/oauth2_proxy  
  
ENTRYPOINT ["oauth2_proxy"]  

