FROM golang:1.8 as builder  
WORKDIR /go/src/github.com/miguellgt/hello-helm/  
COPY . .  
RUN go get -v ./...  
RUN go test -v ./...  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/miguellgt/hello-helm/app .  
EXPOSE 8080  
CMD ["./app"]  

