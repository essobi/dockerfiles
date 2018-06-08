FROM golang:alpine AS build-env  
ADD . /go/src/github.com/podnov/metrotransit  
RUN apk --update add git \  
&& cd /go/src/github.com/podnov/metrotransit \  
&& go get \  
&& go build -o metrotransit  
  
FROM alpine  
RUN adduser -D -u 1000 metrotransit  
COPY \--from=build-env /go/src/github.com/podnov/metrotransit/metrotransit
/metrotransit  
USER metrotransit  
CMD ["/metrotransit","server"]  

