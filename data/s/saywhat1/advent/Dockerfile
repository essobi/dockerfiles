FROM golang:1.8.5-jessie as builder  
  
COPY . /go/src/github.com/derek-elliott/advent-of-code-2017  
  
WORKDIR /go/src/github.com/derek-elliott/advent-of-code-2017  
  
RUN go get -u github.com/golang/dep/cmd/dep && \  
dep ensure && \  
CGO_ENABLED=0 GOGC=off GOOS=linux go build \  
-a -installsuffix nocgo -o advent .  
  
FROM scratch  
COPY \--from=builder /go/src/github.com/derek-elliott/advent-of-
code-2017/advent /  
CMD ["/advent"]  

