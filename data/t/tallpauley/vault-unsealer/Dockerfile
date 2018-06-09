# Multi-stage build (requires Docker 17.05 or greater)  
# for first stage of canary container, we just build the binary  
FROM golang:1.9  
WORKDIR /go/src/app  
ADD main.go .  
  
RUN go-wrapper download  
RUN main_sha1=$(cat main.go | sha1sum | awk '{print $1}') && \  
CGO_ENABLED=0 go build -v -ldflags "-X main.Version=canary-${main_sha1}"  
  
# second stage is just copy the binary from the first stage  
FROM alpine:3.6  
WORKDIR /  
  
COPY \--from=0 /go/src/app/app /vault-unsealer  
RUN apk update && apk add --no-cache ca-certificates && \  
rm -rf /var/cache/apk/* && \  
chmod +x /vault-unsealer  
  
EXPOSE 443  
ENTRYPOINT ["/vault-unsealer"]  
CMD ["-server"]

