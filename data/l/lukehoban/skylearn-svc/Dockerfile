FROM golang:1.7  
RUN mkdir -p /go/src/github.com/lukehoban/skylearn  
WORKDIR /go/src/github.com/lukehoban/skylearn  
  
COPY . /go/src/github.com/lukehoban/skylearn  
  
RUN go get -d -v ./svc  
RUN go install -v -ldflags "-X main.buildstamp=`date -u
'+%Y-%m-%d_%I:%M:%S%p'` -X main.githash=`git rev-parse HEAD`" ./svc  
  
CMD ["/go/bin/svc"]  

