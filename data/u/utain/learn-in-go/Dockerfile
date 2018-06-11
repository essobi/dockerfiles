FROM golang:1.8.3-alpine3.6  
WORKDIR /go/src/learn-in-go  
ADD . /go/src/learn-in-go  
RUN go install learn-in-go  
COPY app.go .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
FROM alpine:3.6  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=0 /go/src/learn-in-go .  
CMD ["./app"]  

