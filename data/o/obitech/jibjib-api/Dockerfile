# Step 1: Building the binary  
FROM golang:1.10 as builder  
  
WORKDIR /go/src/github.com/gojibjib/jibjib-api  
  
RUN go get -d -v github.com/gorilla/mux  
RUN go get -d -v gopkg.in/mgo.v2  
  
COPY pkg ./pkg  
COPY main.go ./  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
# Step 2: Copy & Run  
FROM alpine:latest  
  
WORKDIR /home/app  
  
COPY \--from=builder /go/src/github.com/gojibjib/jibjib-api/app ./  
  
EXPOSE 8080/tcp  
  
CMD ["./app"]

