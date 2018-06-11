FROM golang:1.8.3-alpine  
LABEL maintainer "Nikolas Silva <nikolas.rsilva@gmail.com>"  
  
RUN apk update && apk --no-cache add git  
  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN go get -u github.com/githubnemo/CompileDaemon  

