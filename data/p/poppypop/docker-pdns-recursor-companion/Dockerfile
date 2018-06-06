FROM golang:alpine as builder  
  
RUN set -xe \  
&& apk update --no-cache && apk upgrade --no-cache \  
&& apk add --update --no-cache git \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /go/src/github.com/PoppyPop/docker-pdns-recursor-companion  
COPY ./src/ .  
  
RUN go get -d -v ./...  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o docker-pdns-
recursor-companion .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
  
WORKDIR /app/  
COPY \--from=builder /go/src/github.com/PoppyPop/docker-pdns-recursor-
companion/docker-pdns-recursor-companion .  
CMD ["/app/docker-pdns-recursor-companion"]

