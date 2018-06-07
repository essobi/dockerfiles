FROM golang:1.9.0-alpine  
  
ENV GO15VENDOREXPERIMENT 1  
RUN apk add --no-cache git docker gcc make g++  
RUN go get github.com/Masterminds/glide  
RUN go build github.com/Masterminds/glide  
  
VOLUME /go/src/app  
WORKDIR /go/src  
  
COPY ./build.sh /go/src/  
  
ENTRYPOINT ["./build.sh"]  

