FROM golang:1.6  
WORKDIR /go/src/app  
  
ADD . .  
  
RUN go get ./... && go build  
  
EXPOSE 5555  
CMD ["app"]  

