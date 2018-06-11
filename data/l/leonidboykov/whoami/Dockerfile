FROM golang:1.10 as builder  
WORKDIR /go/src/github.com/leonidboykov/whoami  
COPY . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo .  
  
FROM scratch  
COPY \--from=builder /go/src/github.com/leonidboykov/whoami/whoami /  
EXPOSE 8080  
ENTRYPOINT ["/whoami"]  

