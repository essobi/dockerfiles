FROM golang:1.8.3-alpine3.6 as builder  
WORKDIR /go/src/github.com/mono83/geos  
COPY . .  
RUN apk add --no-cache make git && \  
make release  
  
FROM alpine:latest  
COPY \--from=builder /go/src/github.com/mono83/geos/release/geos-linux64 /geos  
RUN apk --no-cache add ca-certificates && \  
chmod a+x /geos  
EXPOSE 5001 80  
CMD ["/geos", ":5001", ":80"]

