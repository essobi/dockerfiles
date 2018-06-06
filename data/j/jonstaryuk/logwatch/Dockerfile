FROM golang:1-alpine AS compiled  
RUN apk --no-cache add git  
  
WORKDIR /go/src/github.com/jonstaryuk/logwatch  
COPY . .  
RUN go test -timeout 30s github.com/jonstaryuk/logwatch/...  
RUN go install github.com/jonstaryuk/logwatch  
  
FROM alpine  
WORKDIR /app  
COPY \--from=compiled /go/bin/logwatch .  
ENTRYPOINT ["./logwatch"]  

