FROM golang:latest  
  
RUN mkdir /root/go  
RUN apk update && apk upgrade && apk add \--no-cache bash git openssh make  
RUN go get -u github.com/golang/lint/golint  
RUN go get -u github.com/kisielk/errcheck  
RUN go get -u github.com/axw/gocov/gocov  
RUN go get -u github.com/AlekSi/gocov-xml  
RUN go get -u github.com/jstemmer/go-junit-report  
RUN go get -u github.com/jteeuwen/go-bindata/...

