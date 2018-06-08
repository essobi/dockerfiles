FROM golang:1.8.7-alpine3.6  
WORKDIR /go/src/github.com/n-marton/sese/  
COPY main.go .  
COPY Gopkg.lock .  
COPY Gopkg.toml .  
RUN apk update && apk add git  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN dep ensure  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o sese .  
  
FROM alpine:3.7  
RUN apk update && apk add bash && mkdir /app  
COPY \--from=0 /go/src/github.com/n-marton/sese/sese /app/  
  
WORKDIR /app/  
CMD ["./sese"]  

