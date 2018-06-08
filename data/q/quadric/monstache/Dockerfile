FROM golang:1.10.0  
# FROM golang:1.10.0-alpine3.7  
# https://hub.docker.com/_/golang/  
  
# https://rwynn.github.io/monstache-site/start/#installation  
  
# For Elasticsearch 6 use (v4+)  
# RUN go get -u github.com/rwynn/monstache  
  
# # For Elasticsearch before 6 use  
# RUN go get -u gopkg.in/rwynn/monstache.v3  
# This doesn't work for some reason  
  
COPY build-4.1.2/linux-amd64/monstache /go/bin/monstache  
# COPY build-4.1.2/linux-amd64/monstache /usr/local/go/bin/monstache  
  
# TODO Maybe add an entrypoint to monstache binary with params later on  

