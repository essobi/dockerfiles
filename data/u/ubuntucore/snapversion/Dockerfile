FROM golang:alpine  
  
ADD . /go/src/github.com/ubuntu-core/snapversion  
  
RUN apk add --no-cache git  
  
RUN go get github.com/zenazn/goji  
  
RUN go install github.com/ubuntu-core/snapversion/cmd/snapversion  
  
ENTRYPOINT /go/bin/snapversion  
  
EXPOSE 8000  

