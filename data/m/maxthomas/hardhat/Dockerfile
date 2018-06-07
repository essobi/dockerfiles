FROM golang:latest AS builder  
  
WORKDIR /go/src/github.com/maxthomas/hardhat  
  
COPY . .  
  
RUN go get -u github.com/golang/dep/cmd/dep && which dep && dep ensure  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app
cmd/servers/main.go  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
  
WORKDIR /root/  
  
COPY \--from=builder /go/src/github.com/maxthomas/hardhat/app .  
  
CMD [ "./app", "storer" ]  

