FROM golang:1.9 as builder  
MAINTAINER Travis CI GmbH <support+travis-worker-docker-image@travis-ci.org>  
  
RUN go get -u \  
github.com/alecthomas/gometalinter \  
github.com/FiloSottile/gvt \  
mvdan.cc/sh/cmd/shfmt \  
&& gometalinter --install \  
&& apt-get update && apt-get install -y shellcheck  
  
COPY . /go/src/github.com/travis-ci/worker  
WORKDIR /go/src/github.com/travis-ci/worker  
RUN go get ./...  
RUN make build  
  
#################################  
### linux/amd64/travis-worker ###  
#################################  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
  
WORKDIR /root/  
  
COPY --from=builder /go/src/github.com/travis-
ci/worker/build/linux/amd64/travis-worker .  
  
CMD ["./travis-worker"]  

