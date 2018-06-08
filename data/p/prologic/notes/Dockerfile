FROM golang:alpine  
  
EXPOSE 8000/tcp  
  
ENTRYPOINT ["notes"]  
  
RUN \  
apk add --update git && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /go/src/notes  
WORKDIR /go/src/notes  
  
COPY . /go/src/notes  
  
RUN go get -v -d  
RUN go get github.com/GeertJohan/go.rice/rice  
RUN rice embed-go  
RUN go install -v  

