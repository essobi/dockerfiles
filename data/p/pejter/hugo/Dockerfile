FROM golang:latest AS build  
  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
  
RUN go get github.com/magefile/mage  
RUN go get -d github.com/gohugoio/hugo  
RUN cd ${GOPATH:-/go}/src/github.com/gohugoio/hugo \  
&& mage vendor \  
&& mage install  
  
FROM alpine:latest  
WORKDIR /site  
RUN apk --no-cache add ca-certificates py-pygments  
COPY \--from=0 /go/bin/hugo /usr/local/bin/hugo  
ENTRYPOINT ["hugo"]  

