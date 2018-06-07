FROM golang:1.10-alpine as builder  
WORKDIR /usr/local/go/src/github.com/LendicoCH/ranking  
COPY . /usr/local/go/src/github.com/LendicoCH/ranking  
RUN apk add --update make  
RUN make build.linux  
  
FROM scratch  
COPY \--from=builder /usr/local/go/src/github.com/LendicoCH/ranking/ranking
/ranking  
COPY \--from=builder /usr/local/go/src/github.com/LendicoCH/ranking/swagger
/swagger  
ENTRYPOINT ["/ranking"]  

