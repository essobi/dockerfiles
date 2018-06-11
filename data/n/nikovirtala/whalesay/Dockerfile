FROM golang:alpine as build  
  
WORKDIR /whalesay  
ADD . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o whalesay .  
  
FROM alpine:edge  
LABEL maintainer "Niko Virtala <niko@nikovirtala.io>"  
  
RUN adduser -D -g '' -h /home/nikovirtala nikovirtala  
USER nikovirtala  
WORKDIR /home/nikovirtala  
  
COPY \--from=build /whalesay .  
EXPOSE 8080  
ENTRYPOINT ["./whalesay"]  
  

