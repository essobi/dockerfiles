FROM ubuntu:16.04  
# Downloaded from
https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip  
# VERSION 3.2.0  
COPY bin/protoc /usr/local/bin/  
COPY include/google /usr/local/include/  
  
# Built using:  
# go version go1.7 darwin/amd64  
# git clone https://github.com/golang/protobuf  
# cd protobuf/protoc-gen-go  
# git rev-parse HEAD  
# > 2bba0603135d7d7f5cb73b2125beeda19c09f4ef  
# GOOS=linux GOARH=amd64 go build  
COPY bin/protoc-gen-go /usr/local/bin/  
  

