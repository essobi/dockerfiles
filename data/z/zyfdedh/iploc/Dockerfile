FROM golang:1.8  
ENV PROJECT $GOPATH/src/github.com/zyfdegh/iploc  
WORKDIR $PROJECT  
  
COPY . $PROJECT  
  
RUN go test $(go list ./... | grep -v /vendor/) && \  
go build -o bin/iploc && \  
cp index.tpl bin/  
  
EXPOSE 80  
CMD ["./bin/iploc"]  

