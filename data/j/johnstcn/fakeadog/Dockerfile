FROM golang:alpine as builder  
WORKDIR /go/src/github.com/johnstcn/fakeadog  
ADD . /go/src/github.com/johnstcn/fakeadog  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o fakeadog .  
  
FROM alpine:latest  
MAINTAINER Cian Johnston <public@cianjohnston.ie>  
  
ENV HOST 0.0.0.0  
ENV PORT 8125  
EXPOSE 8125/udp  
  
WORKDIR /root  
COPY \--from=builder /go/src/github.com/johnstcn/fakeadog/fakeadog .  
  
CMD ["./fakeadog"]  

