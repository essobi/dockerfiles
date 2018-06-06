FROM golang:alpine AS build  
  
RUN \  
apk add --update git && \  
rm -rf /var/cache/apk/*  
  
ADD . /src  
  
WORKDIR /src  
RUN go get -v -d ./...  
RUN go get github.com/GeertJohan/go.rice/rice  
RUN rice embed-go  
RUN go build -o app  
  
FROM alpine  
COPY \--from=build /src/app /app  
  
EXPOSE 8000/tcp  
  
ENTRYPOINT /app  
CMD []  

