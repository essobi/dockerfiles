FROM alpine:3.7  
  
ENV GOLANG_VERSION 1.10  
ENV GOPATH /go  
  
RUN set -eux; \  
apk add --no-cache ca-certificates; \  
apk add --no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go \  
; \  
export \  
# set GOROOT_BOOTSTRAP such that we can actually build Go  
GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
# ... and set "cross-building" related vars to the installed system's values
so that we create a build targeting the proper arch  
# (for example, if our build host is GOARCH=amd64, but our build env/image is
GOARCH=386, our build needs GOARCH=386)  
GOOS="$(go env GOOS)" \  
GOARCH="$(go env GOARCH)" \  
GOHOSTOS="$(go env GOHOSTOS)" \  
GOHOSTARCH="$(go env GOHOSTARCH)" \  
; \  
# also explicitly set GO386 and GOARM if appropriate  
# https://github.com/docker-library/golang/issues/184  
apkArch="$(apk --print-arch)"; \  
case "$apkArch" in \  
armhf) export GOARM='6' ;; \  
x86) export GO386='387' ;; \  
esac; \  
\  
wget -O go.tgz "https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz"; \  
echo 'f3de49289405fda5fd1483a8fe6bd2fa5469e005fd567df64485c4fa000c7f24
*go.tgz' | sha256sum -c -; \  
tar -C /usr/local -xzf go.tgz; \  
rm go.tgz; \  
\  
cd /usr/local/go/src; \  
./make.bash; \  
\  
apk del .build-deps; \  
\  
export PATH="/usr/local/go/bin:$PATH"; \  
go version; \  
\  
\  
mkdir -p "$GOPATH/src" "$GOPATH/bin"; \  
chmod -R 777 "$GOPATH"; \  
\  
\  
apk add --update git; \  
go get -d github.com/devcodewak/avonsg_openshift/cmd; \  
go build -ldflags="-s -w" -o /go/bin/web
github.com/devcodewak/avonsg_openshift/cmd; \  
rm -rf /go/src/github.com/; \  
rm -rf /usr/local/go/; \  
apk del git; \  
rm -rf /var/cache/apk/* /tmp/*; \  
\  
\  
export PATH="$GOPATH/bin:$PATH"; \  
/go/bin/web -version  
  
  
ENV PATH $GOPATH/bin:$PATH  
WORKDIR $GOPATH  
  
CMD ["/go/bin/web", "-server", "-cmd", "-key",
"809240d3a021449f6e67aa73221d42df942a308a", "-listen", "http2://:8443",
"-listen", "http://:8444", "-log", "null"]  
EXPOSE 8443 8444

