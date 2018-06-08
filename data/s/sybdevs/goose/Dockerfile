FROM golang:1.4  
  
RUN mkdir -p /go/src/github.com/syb-devs/goose  
  
COPY . /go/src/github.com/syb-devs/goose  
  
WORKDIR /go/src/github.com/syb-devs/goose/http/server  
  
RUN go get  
RUN go build .  
  
ENV PORT 80  
EXPOSE 80  
  
CMD ./server

