FROM golang:1.10.2  
WORKDIR /go/src/env-api  
COPY . .  
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-X main.version=v1.0.0" .  
  
FROM scratch  
COPY \--from=0 /go/src/env-api/env-api .  
ENTRYPOINT ["/env-api"]  

