# LiveRecord GoLang application  
FROM golang:1.9  
LABEL maintainer = "philipp@zoonman.com"  
  
WORKDIR /go/src/app  
  
COPY . .  
  
RUN go get -d -v ./...  
RUN go build  
  
ENTRYPOINT ["./server"]

