FROM golang:alpine AS build-env  
WORKDIR /usr/local/go/src/github.com/rusenask/cloudstore  
COPY . /usr/local/go/src/github.com/rusenask/cloudstore  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
RUN cd cmd/cloudstore && go install  
  
FROM alpine:latest  
RUN apk add --no-cache ca-certificates  
COPY \--from=build-env /usr/local/go/bin/cloudstore /bin/cloudstore  
CMD ["cloudstore"]  

