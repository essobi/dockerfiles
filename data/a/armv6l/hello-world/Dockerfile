# Copied from
https://github.com/prometheus/client_golang/blob/master/examples/simple/Dockerfile  
FROM golang:1.9.2-alpine AS builder  
WORKDIR /go/src/github.com/infrastructure-as-code/docker-hello-world  
ENV GIN_MODE debug  
COPY Makefile *.go ./  
RUN apk update && \  
apk upgrade && \  
apk add \  
git \  
make && \  
make all  
  
FROM scratch  
LABEL maintainer "Vince Tse <vincetse@users.noreply.github.com>"  
COPY \--from=builder /go/src/github.com/infrastructure-as-code/docker-hello-
world/hello_world .  
ENV GIN_MODE release  
EXPOSE 8080  
ENTRYPOINT ["/hello_world"]  

