FROM golang:1.10.2-alpine3.7  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh  
  
RUN go get -u github.com/canthefason/go-watcher  
RUN go install github.com/canthefason/go-watcher/cmd/watcher  
  
ENV GOPATH /go  
ENV APP_PATH app  
  
WORKDIR ${GOTPATH}/src/${APP_PATH}  
  
CMD ["watcher"]

