# Dockerfile for Golang  
  
FROM golang:1.7  
MAINTAINER Hiroaki Egashira  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
RUN go get -u github.com/labstack/echo\  
&& go get -u github.com/jinzhu/gorm  

