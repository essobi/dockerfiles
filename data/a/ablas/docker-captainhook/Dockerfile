FROM ubuntu:latest  
  
MAINTAINER Arturo Blas Jimenez "arturoblas@gmail.com"  
RUN apt-get update  
  
RUN apt-get upgrade -y  
  
RUN apt-get install -y git-core golang  
  
ENV GOPATH /gosource  
  
RUN go get github.com/bketelsen/captainhook  
  
EXPOSE 8080  
  
ENTRYPOINT ["/gosource/bin/captainhook", "-listen-addr=0.0.0.0:8080",
"-configdir=/webhooks"]  

