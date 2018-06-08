FROM golang:1.9.2-alpine3.7  
  
ENV GOPATH /go  
  
RUN set -ex \  
&& apk \--no-cache add git gcc libc-dev \  
&& mkdir -p \  
/go/src/bitbucket.org/liamstask \  
/go/src/github.com/cloudflare \  
&& cd /go/src/bitbucket.org/liamstask \  
&& git clone https://bitbucket.org/liamstask/goose.git \  
&& cd goose && mkdir bin && cd bin \  
&& go get ../cmd/goose && go build ../cmd/goose \  
&& cd /go/src/github.com/cloudflare \  
&& git clone https://github.com/cloudflare/cfssl.git \  
&& cd cfssl \  
&& go get github.com/GeertJohan/go.rice/rice && rice embed-go -i=./cli/serve \  
&& mkdir -p bin && cd bin \  
&& go build ../cmd/cfssl \  
&& go build ../cmd/cfssljson \  
&& go build ../cmd/mkbundle \  
&& go build ../cmd/multirootca \  
&& echo "Build complete."  
  
FROM alpine:3.7  
RUN mkdir -p /src/cfssl/certdb/pg /src/cfssl/certdb/mysql
/src/cfssl/certdb/sqlite  
COPY --from=0
/go/src/github.com/cloudflare/cfssl/vendor/github.com/cloudflare/cfssl_trust
/etc/cfssl  
COPY \--from=0 /go/src/github.com/cloudflare/cfssl/bin/ /usr/bin  
COPY --from=0 /go/src/bitbucket.org/liamstask/goose/bin/ /usr/bin  
COPY \--from=0 /go/src/github.com/cloudflare/cfssl/certdb/pg/
/src/cfssl/certdb/pg  
COPY \--from=0 /go/src/github.com/cloudflare/cfssl/certdb/mysql/
/src/cfssl/certdb/mysql  
COPY \--from=0 /go/src/github.com/cloudflare/cfssl/certdb/sqlite/
/src/cfssl/certdb/sqlite  
COPY ./docker-entrypoint.sh /usr/bin/  
  
RUN set -ex \  
&& apk add --update ca-certificates \  
&& update-ca-certificates \  
&& apk add \  
su-exec \  
&& rm -rf /var/cache/apk/* \  
&& addgroup -S cfssl && adduser -S -G cfssl cfssl \  
&& chmod +x /usr/bin/docker-entrypoint.sh  
  
VOLUME [ "/etc/cfssl", "/var/lib/redoctober/data" ]  
  
WORKDIR /etc/cfssl  
  
EXPOSE 8888  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["cfssl", "--help"]  

