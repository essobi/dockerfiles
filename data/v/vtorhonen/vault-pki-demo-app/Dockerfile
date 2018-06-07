FROM golang:1.9-alpine3.7  
WORKDIR /go/src/app  
COPY . .  
  
RUN go get -d -v ./...  
RUN go install -v ./...  
  
CMD ["app"]  

