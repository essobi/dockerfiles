# Build stage  
FROM golang:alpine AS build-env  
ADD . $GOPATH/src/github.com/aiotrc/uplink  
RUN apk update && apk add git  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN cd $GOPATH/src/github.com/aiotrc/uplink/ && dep ensure && go build -v -o
/uplink  
  
# Final stage  
FROM alpine  
RUN apk add --no-cache tzdata  
WORKDIR /app  
COPY \--from=build-env /uplink /app/  
ENTRYPOINT ["./uplink"]  

