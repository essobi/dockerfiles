FROM golang:alpine  
  
EXPOSE 8000/tcp  
  
ENTRYPOINT ["webdavd"]  
  
RUN \  
apk add --update git && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /go/src/webdavd  
WORKDIR /go/src/webdavd  
  
COPY . /go/src/webdavd  
  
RUN go get -v -d  
RUN go get github.com/GeertJohan/go.rice/rice  
RUN rice embed-go  
RUN go install -v  

