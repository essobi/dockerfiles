FROM golang:latest as builder  
MAINTAINER Stephan Kirsten <vebis@gmx.net>  
LABEL description="trigger-proxy builder container"  
WORKDIR /src/  
COPY ./assets/build/app.go .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
FROM alpine:latest  
MAINTAINER Stephan Kirsten <vebis@gmx.net>  
LABEL description="trigger-proxy docker container"  
WORKDIR /root/  
COPY \--from=builder /src/app .  
COPY ./assets/run/example.csv mapping.csv  
CMD [ "./app" ]  

