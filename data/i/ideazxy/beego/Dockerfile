# Base image is in https://registry.hub.docker.com/_/golang/  
# Refer to https://blog.golang.org/docker for usage  
FROM golang:1.3.3  
MAINTAINER Yudi smartzxy@gmail.com  
  
# Install beego & bee  
RUN go get -u github.com/astaxie/beego  
RUN go get -u github.com/beego/bee  
# Install driver for mongoDB  
RUN go get -u gopkg.in/mgo.v2  
# Install UUID lib  
RUN go get -u code.google.com/p/go-uuid/uuid  

