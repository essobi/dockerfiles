FROM golang:1  
RUN go get -d -v github.com/XS4ALL/imaptar  
WORKDIR /go/src/github.com/XS4ALL/imaptar  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o imaptar .  
  
FROM alpine:latest  
LABEL maintainer "martijn.pepping@automiq.nl"  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=0 /go/src/github.com/XS4ALL/imaptar/imaptar .  
ENTRYPOINT ["./imaptar"]  

