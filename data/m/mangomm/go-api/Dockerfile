FROM golang:1.8.3-alpine3.6  
WORKDIR /go/src/github.com/AhmetS/go-api  
COPY . .  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh && \  
rm -f /var/cache/apk/*  
RUN go get -u github.com/golang/dep/cmd/dep && \  
dep ensure && \  
env GOOS=linux GOARCH=amd64 go build -o linux.server
/go/src/github.com/AhmetS/go-api/main.go  
EXPOSE 8000  
CMD ["./linux.server"]  

