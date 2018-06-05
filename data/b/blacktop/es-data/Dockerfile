FROM alpine:3.6  
LABEL maintainer "https://github.com/blacktop"  
  
ENV STACK 5.0.0  
ENV BULK_SIZE 5242880  
COPY main.go /go/src/main.go  
RUN apk add --no-cache -t .build-deps \  
ca-certificates \  
build-base \  
mercurial \  
musl-dev \  
openssl \  
wget \  
bash \  
git \  
go \  
&& set -x \  
&& echo "Build [import-dashboard] Go binary..." \  
&& export GOPATH=/go \  
&& go version \  
&& git clone -b v$STACK https://github.com/elastic/beats.git
$GOPATH/src/github.com/elastic/beats \  
&& cd $GOPATH/src/github.com/elastic/beats/libbeat/dashboards \  
&& go build -ldflags "-s -w -X main.beat=" -o import_dashboards \  
&& mv import_dashboards /bin/import_dashboards \  
&& echo "Building [ingest] Go binary..." \  
&& cd /go/src/ \  
&& export GOPATH=/go \  
&& go version \  
&& go get -d \  
&& go build -ldflags="-s -w" -o /bin/ingest \  
&& rm -rf /go /usr/local/go /usr/lib/go /tmp/* \  
&& apk del --purge .build-deps  
  
COPY nginx_data/data.zip /nginx_data/data.zip  
COPY load.sh /load.sh  
  
ENTRYPOINT ["/load.sh"]  

