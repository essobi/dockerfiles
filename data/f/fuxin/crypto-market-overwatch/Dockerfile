FROM golang:1.9 AS build  
WORKDIR /go/src/github.com/FX-HAO/crypto-market-overwatch  
ADD . /go/src/github.com/FX-HAO/crypto-market-overwatch  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o crypto-market-
overwatch .  
  
FROM ubuntu  
RUN apt-get update && apt-get install -y ca-certificates  
WORKDIR /app  
COPY \--from=build /go/src/github.com/FX-HAO/crypto-market-overwatch .  
EXPOSE 80  
CMD ["/app/crypto-market-overwatch", "-H", "0.0.0.0", "-p", "80", "-i", "30"]

