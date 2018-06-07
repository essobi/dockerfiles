FROM golang:1.6-alpine  
MAINTAINER Thibaud Lepretre <thibaud.lepretre@gmail.com>  
  
RUN apk add \--no-cache git && \  
cd /go/src && \  
git clone -b commands_with_arguments https://github.com/oker1/go-gitlab-
webhook.git && \  
cd go-gitlab-webhook && \  
go get -d -v && \  
go install -v && \  
cd .. && \  
rm -fr go-gitlab-webhook/ && \  
apk del git  
  
EXPOSE 3344  
ENTRYPOINT ["go-gitlab-webhook"]

