FROM golang:alpine  
  
EXPOSE 8000/tcp  
  
ENTRYPOINT ["wiki"]  
  
RUN \  
apk add --update git && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /go/src/wiki  
WORKDIR /go/src/wiki  
  
COPY . /go/src/wiki  
  
RUN go get -v -d  
RUN go get github.com/GeertJohan/go.rice/rice  
RUN rice embed-go  
RUN go install -v  

