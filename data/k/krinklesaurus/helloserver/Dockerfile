FROM golang:1.8.3-alpine  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
  
WORKDIR /go/src/app  
  
COPY . .  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run", "helloserver"]  
  
EXPOSE 8080  

