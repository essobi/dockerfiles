FROM golang:1.9.1  
WORKDIR /go/src/app  
COPY . .  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
ENV GIN_MODE release  
  
CMD ["go-wrapper", "run"]

