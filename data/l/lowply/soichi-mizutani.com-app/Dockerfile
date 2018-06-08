FROM golang:latest AS builder  
WORKDIR /go/src/app  
COPY . .  
RUN go-wrapper download  
RUN go-wrapper install  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .  
  
FROM alpine:latest  
COPY \--from=builder /go/src/app/main .  
COPY ./templates ./templates  
COPY ./data.json ./data.json  
CMD ["./main"]  
  
MAINTAINER Sho Mizutani <lowply@gmail.com>  

