FROM golang:1.9-alpine3.6  
WORKDIR /go/src/app  
ADD . .  
RUN apk add --update-cache git glide; glide install -v  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-s' -o
main  
FROM alpine:3.6  
COPY \--from=0 /go/src/app/main /main  
ENTRYPOINT /main  
CMD ["-config", "/config.yml"]

