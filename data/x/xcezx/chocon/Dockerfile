FROM golang:1.9-alpine as build  
  
RUN apk add --update --no-cache git  
RUN go get -v -u github.com/kazeburo/chocon  
  
FROM alpine:3.6  
COPY \--from=build /go/bin/chocon /usr/local/bin/chocon  
  
RUN apk add --update --no-cache ca-certificates  
  
ENTRYPOINT ["/usr/local/bin/chocon"]  
  
EXPOSE 3000  

