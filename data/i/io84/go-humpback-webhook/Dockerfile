FROM golang:1.8.3-alpine  
  
WORKDIR /go/src/app  
COPY webhook.go webhook.go  
  
RUN apk add git --no-cache  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]  

