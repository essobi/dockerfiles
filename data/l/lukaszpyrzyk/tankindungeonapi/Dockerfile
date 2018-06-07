FROM golang:alpine  
  
MAINTAINER Lukasz Pyrzyk <lukasz.pyrzyk@gmail.com>  
  
# install git  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh  
  
ADD . /go/src/github.com/lukasz-pyrzyk/TankInDungeonApi  
  
RUN go get github.com/ant0ine/go-json-rest/rest  
RUN go get gopkg.in/mgo.v2  
  
RUN go install github.com/lukasz-pyrzyk/TankInDungeonApi/api  
  
ENTRYPOINT ["/go/bin/api"]  
  
EXPOSE 8080  

