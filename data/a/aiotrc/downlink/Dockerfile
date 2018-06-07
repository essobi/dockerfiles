# Build stage  
FROM golang:alpine AS build-env  
ADD . $GOPATH/src/github.com/aiotrc/downlink  
RUN apk update && apk add git  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN cd $GOPATH/src/github.com/aiotrc/downlink/ && dep ensure && go build -v -o
/downlink  
  
# Final stage  
FROM alpine  
WORKDIR /app  
COPY \--from=build-env /downlink /app/  
ENTRYPOINT ["./downlink"]  

