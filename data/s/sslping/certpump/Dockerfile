FROM golang:1.10-alpine3.7 as builder  
RUN apk update && apk add ca-certificates git && rm -rf /var/cache/apk/*  
  
# setup the working directory  
WORKDIR /go/src/github.com/chrisDeFouRire/CertPump  
COPY . .  
  
RUN go get github.com/nats-io/go-nats  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o CertPump
./CertPump.go  
  
# use a minimal alpine image  
FROM alpine:3.7  
# add ca-certificates in case you need them  
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*  
# set working directory  
WORKDIR /root  
# copy the binary from builder  
COPY \--from=builder /go/src/github.com/chrisDeFouRire/CertPump/CertPump .  
# run the binary  
CMD ["./CertPump"]  

