FROM golang:alpine  
  
LABEL maintainer "jinlin.gan@gmail.com"  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh gcc g++  
  
RUN go get github.com/Masterminds/glide  
  
RUN go get github.com/golang/dep/cmd/dep  
  
RUN go get github.com/derekparker/delve/cmd/dlv

