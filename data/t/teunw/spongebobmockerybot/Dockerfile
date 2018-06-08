FROM golang:alpine  
WORKDIR /go/src/app  
COPY . .  
COPY ./src .  
  
RUN apk update && apk upgrade && apk add --no-cache bash git openssh  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]

