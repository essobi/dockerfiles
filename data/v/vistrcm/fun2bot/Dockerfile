FROM golang:1.8  
RUN mkdir -p /go/src/github.com/vistrcm/fun2bot  
WORKDIR /go/src/github.com/vistrcm/fun2bot  
COPY . .  
  
RUN go-wrapper download # "go get -d -v ./..."  
RUN go-wrapper install # "go install -v ./..."  
  
ENTRYPOINT ["go-wrapper", "run"]  

