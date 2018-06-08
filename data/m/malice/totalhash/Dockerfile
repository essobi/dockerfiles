FROM malice/alpine  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-
plugins/totalhash.git"  
LABEL malice.plugin.category="intel"  
LABEL malice.plugin.mime="hash"  
LABEL malice.plugin.docker.engine="*"  
  
COPY . /go/src/github.com/malice-plugins/totalhash  
RUN apk --update add --no-cache ca-certificates  
RUN apk --update add --no-cache -t .build-deps \  
build-base \  
mercurial \  
musl-dev \  
openssl \  
bash \  
wget \  
git \  
gcc \  
go \  
&& echo "===> Building totalhash Go binary..." \  
&& cd /go/src/github.com/malice-plugins/totalhash \  
&& export GOPATH=/go \  
&& go version \  
&& go get -v \  
&& CGO_ENABLED=0 \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/totalhash \  
&& rm -rf /go /usr/local/go /usr/lib/go /tmp/* \  
&& apk del --purge .build-deps  
  
WORKDIR /malware  
  
ENTRYPOINT ["su-exec","malice","/sbin/tini","--","totalhash"]  
CMD ["--help"]  

