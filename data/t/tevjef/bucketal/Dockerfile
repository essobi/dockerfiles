FROM golang:1.9-alpine AS build-env  
COPY . /go/src/github.com/prolificinteractive/bucketal  
  
ENV PATH /go/bin:$PATH  
  
RUN apk --no-cache add ca-certificates openssl git && \  
update-ca-certificates && \  
go get -u github.com/golang/dep/cmd/dep && \  
cd /go/src/github.com/prolificinteractive/bucketal && \  
dep ensure -v  
  
WORKDIR /go/src/github.com/prolificinteractive/bucketal  
  
RUN go install -v github.com/prolificinteractive/bucketal  
  
FROM alpine  
ENV PATH /:$PATH  
WORKDIR /  
RUN apk --no-cache add ca-certificates openssl && \  
update-ca-certificates  
COPY \--from=build-env /go/bin/bucketal /  
CMD ["bucketal"]

