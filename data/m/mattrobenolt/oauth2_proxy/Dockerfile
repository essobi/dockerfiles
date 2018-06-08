FROM alpine:3.3  
  
ENV OAUTH2_PROXY_REPO bitly/oauth2_proxy  
ENV OAUTH2_PROXY_COMMIT 42f1651ba5ab411e3216bd46f3c90bab153a2f13  
  
RUN set -ex \  
\  
&& export GOLANG_VERSION=1.6 \  
&& export GOLANG_SRC_URL=https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz \  
&& export
GOLANG_SRC_SHA256=a96cce8ce43a9bf9b2a4c7d470bc7ee0cb00410da815980681c8353218dcf146
\  
\  
&& export GOLANG_BOOTSTRAP_VERSION=1.4.3 \  
&& export
GOLANG_BOOTSTRAP_URL=https://golang.org/dl/go$GOLANG_BOOTSTRAP_VERSION.src.tar.gz
\  
&& export GOLANG_BOOTSTRAP_SHA1=486db10dc571a55c8d795365070f66d343458c48 \  
\  
&& apk add --no-cache --virtual .build-deps \  
bash \  
ca-certificates \  
gcc \  
musl-dev \  
openssl \  
tar \  
git \  
&& mkdir -p /usr/local/bootstrap \  
&& wget -q "$GOLANG_BOOTSTRAP_URL" -O golang.tar.gz \  
&& echo "$GOLANG_BOOTSTRAP_SHA1 golang.tar.gz" | sha1sum -c - \  
&& tar -C /usr/local/bootstrap -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/bootstrap/go/src \  
&& ./make.bash \  
&& export GOROOT_BOOTSTRAP=/usr/local/bootstrap/go \  
\  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/go/src \  
&& ./make.bash \  
\  
&& rm -rf /usr/local/bootstrap /usr/local/go/pkg/bootstrap \  
\  
&& mkdir -p /usr/src/oauth2_proxy \  
&& mkdir -p /go \  
&& export GOPATH=/go GOBIN=/usr/local/bin PATH=/go/bin:/usr/local/go/bin:$PATH
\  
&& cd /usr/src/oauth2_proxy \  
&& wget
"https://github.com/${OAUTH2_PROXY_REPO}/archive/${OAUTH2_PROXY_COMMIT}.tar.gz"
-O oauth2_proxy.tar.gz \  
&& tar -C /usr/src/oauth2_proxy -xzf oauth2_proxy.tar.gz --strip-components=1
\  
&& go get -v -d \  
&& go install -v \  
&& rm -rf /go /usr/src/oauth2_proxy /usr/local/go \  
&& apk del .build-deps  
  
EXPOSE 4180  
ENTRYPOINT [ "/usr/local/bin/oauth2_proxy" ]  
CMD [ "-help" ]  

