ARG user=iwaseyusuke  
  
# Stage 0  
FROM golang:1.9-alpine  
USER root  
WORKDIR /root  
RUN apk add \--no-cache \  
gcc \  
git \  
linux-headers \  
musl-dev \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& go get -d github.com/osrg/gobgp \  
# HACK: "go get" will return 1 due to no Go files in "github.com/osrg/gobgp",  
# here uses "||" to avoid failure of building Docker image.  
|| cd ${GOPATH}/src/github.com/osrg/gobgp \  
&& dep ensure -v \  
&& go install ./gobgp \  
&& go install ./gobgpd  
  
# Stage 1  
FROM alpine  
USER root  
WORKDIR /root  
COPY \--from=0 /go/bin/gobgp /usr/local/bin/.  
COPY \--from=0 /go/bin/gobgpd /usr/local/bin/.  
  

