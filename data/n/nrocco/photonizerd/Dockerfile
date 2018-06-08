FROM golang:1.9-alpine AS builder  
WORKDIR /go/src/github.com/nrocco/photonizer  
COPY main.go bindata.go ./  
RUN CGO_ENABLED=0 go build -a -tags netgo -installsuffix netgo -ldflags "-d -s
-w" -o photonizer github.com/nrocco/photonizer  
  
FROM scratch  
COPY \--from=builder /go/src/github.com/nrocco/photonizer/photonizer /  
EXPOSE 8080  
WORKDIR /collection  
VOLUME /collection  
ENTRYPOINT ["/photonizer"]  

