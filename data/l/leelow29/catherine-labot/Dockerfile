FROM golang:1.8  
WORKDIR /go/src/app  
COPY . .  
  
VOLUME /go/src/app/config  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]  

