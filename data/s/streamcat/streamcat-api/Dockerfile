FROM golang:1.7-alpine  
  
EXPOSE 4000  
ADD . /go/src/streamcat-api  
  
RUN apk add --update ca-certificates git gcc g++ && \  
rm -rf /var/cache/apk/* && \  
cd /go/src/streamcat-api && \  
go get -d -v ./... && \  
go build -o /usr/bin/streamcat-api . && \  
cp /go/src/streamcat-api/defaults.json /defaults.json && \  
apk del git gcc g++ && \  
rm -rf /var/cache/apk/* && \  
rm -rf /go  
  
WORKDIR /  
  
CMD ["/usr/bin/streamcat-api"]  

