FROM golang:alpine as builder  
  
ENV HORIZON_VERSION=horizon-v0.12.3  
  
  
RUN apk add \--no-cache git gcc linux-headers musl-dev glide mercurial \  
&& mkdir -p /go/src/github.com/stellar/ \  
&& git clone https://github.com/stellar/go.git /go/src/github.com/stellar/go \  
&& cd /go/src/github.com/stellar/go \  
&& git checkout $HORIZON_VERSION \  
&& glide install \  
&& go install github.com/stellar/go/services/horizon  
  
  
FROM alpine:latest  
  
COPY --from=builder /go/bin/horizon /usr/local/bin/horizon  
  
EXPOSE 8000  
  
ENTRYPOINT ["/usr/local/bin/horizon"]  

