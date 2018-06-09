# Build  
FROM golang:1.9.0-alpine as builder  
  
RUN apk add --no-cache git  
  
WORKDIR /go/src/github.com/thisiserico/devcdn  
COPY . .  
  
RUN go get -d -v ./...  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o devcdn .  
  
# Run  
FROM scratch  
  
COPY \--from=builder /go/src/github.com/thisiserico/devcdn/devcdn .  
  
CMD ["./devcdn"]  
  

