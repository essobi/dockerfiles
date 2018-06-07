# build stage  
FROM golang:alpine AS build-env  
RUN apk update && apk add git  
ADD . /src  
RUN cd /src && go get -d ./... && go build -o goapp  
  
# final stage  
FROM alpine  
WORKDIR /app  
COPY \--from=build-env /src/goapp /app/  
ENTRYPOINT ./goapp

