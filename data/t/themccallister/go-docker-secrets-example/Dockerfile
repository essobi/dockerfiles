FROM golang:1.8-alpine  
  
# install some dependencies  
RUN apk update && apk upgrade && \  
apk add \--no-cache git  
  
RUN mkdir /app  
  
ADD . /app/  
  
WORKDIR /app  
  
# install go deps  
RUN go get -v github.com/gin-contrib/gzip \  
github.com/gin-gonic/gin  
  
RUN go build -o devshare .  
  
CMD ["/app/devshare"]

