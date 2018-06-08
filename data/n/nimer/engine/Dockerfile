FROM golang:1.9.2-alpine3.6  
RUN apk update && \  
apk upgrade && \  
apk add git  
RUN go get github.com/modest-sql/engine  
WORKDIR /go/src/github.com/modest-sql/engine  
RUN mkdir databases  
RUN go build  
CMD ./engine  
EXPOSE 3333  

