FROM golang:alpine  
  
RUN apk --no-cache --update add git  
RUN go get github.com/prometheus/common/log  
Add . /go/src/pushprox/  
WORKDIR /go/src/pushprox/proxy  
RUN go build  
  
EXPOSE 8080  
  
CMD ["./proxy"]

