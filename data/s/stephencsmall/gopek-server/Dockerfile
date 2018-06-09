FROM golang:1.9.2  
WORKDIR /go/src/app  
COPY server.go .  
  
RUN go-wrapper download # "go get -d -v ./..."  
RUN go-wrapper install # "go install -v ./..."  
  
CMD ["go-wrapper", "run"]

