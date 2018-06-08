#  
# Go with gin-gonic/gin running on Alpine Linux image  
#  
FROM golang:1.9.2-alpine  
MAINTAINER IFlavours's Docker Team <docker@iflavours.nl>  
LABEL Description="This image is used to start the Shopr Redirect Service"
Vendor="IFlavours" Version="0.3.0"  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
ENV LANG C.UTF-8  
RUN apk --update add --no-cache bash git  
RUN go get github.com/gin-gonic/gin  

