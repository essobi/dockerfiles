# BUILD  
FROM golang:alpine as builder  
COPY abby.go /go/src/abby/  
WORKDIR /go/src/abby/  
  
RUN apk update && apk add git  
RUN go get  
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags '-s -w' -gcflags=-trimpath=x/y
-o abby abby.go  
ENTRYPOINT ["/bin/true"]  
  
# RELEASE  
FROM alpine:latest  
COPY \--from=builder /go/src/abby/abby .  
  
EXPOSE 5000  
ENTRYPOINT ["./abby"]  

