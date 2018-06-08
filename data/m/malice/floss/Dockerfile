FROM malice/alpine  
  
LABEL maintainer "https://github.com/blacktop"  
  
LABEL malice.plugin.repository = "https://github.com/malice-plugins/floss.git"  
LABEL malice.plugin.category="pe"  
LABEL malice.plugin.mime="application/x-dosexec"  
LABEL malice.plugin.docker.engine="*"  
  
RUN apk --update add --no-cache python py-setuptools  
RUN apk --update add --no-cache -t .build-deps \  
python-dev \  
build-base \  
musl-dev \  
openssl \  
py-pip \  
&& echo "===> Install FLOSS..." \  
&& export PIP_NO_CACHE_DIR=off \  
&& export PIP_DISABLE_PIP_VERSION_CHECK=on \  
&& pip install https://github.com/williballenthin/vivisect/zipball/master \  
&& pip install https://github.com/fireeye/flare-floss/zipball/master \  
&& rm -rf /tmp/* \  
&& apk del --purge .build-deps  
  
COPY . /go/src/github.com/maliceio/malice-floss  
WORKDIR /go/src/github.com/maliceio/malice-floss  
RUN echo "===> Building scan Go binary..." \  
&& apk --update add --no-cache -t .build-deps \  
python-dev \  
build-base \  
mercurial \  
musl-dev \  
openssl \  
py-pip \  
bash \  
wget \  
git \  
gcc \  
go \  
&& export GOPATH=/go \  
&& go version \  
&& go get -v \  
&& go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date
-u +%Y%m%d)" -o /bin/scan \  
&& rm -rf /go /usr/local/go /usr/lib/go /tmp/* \  
&& apk del --purge .build-deps  
  
WORKDIR /malware  
  
ENTRYPOINT ["su-exec","malice","/sbin/tini","--","scan"]  
CMD ["--help"]  

