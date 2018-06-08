FROM golang:1.9.4 as builder  
WORKDIR /go/src/github.com/go-spirit  
RUN go get -v github.com/go-spirit/go-spirit  
RUN cd go-spirit && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o
go-spirit .  
  
FROM golang:1.9.4-alpine3.6  
RUN apk --no-cache add ca-certificates git openssh  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/go-spirit/go-spirit/go-spirit /usr/bin  
CMD ["go-spirit"]

