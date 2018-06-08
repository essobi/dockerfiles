FROM debian as builder  
  
ARG VERSION=4.4.3  
ARG CC=""  
ARG CC_PKG=""  
ARG CC_GOARCH=""  
ENV GOPATH=/go  
WORKDIR /go/src/github.com/grafana/grafana  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
git \  
golang-1.8 \  
wget \  
ca-certificates \  
gcc \  
libc6-dev \  
xz-utils \  
bzip2 \  
$CC_PKG \  
&& ln -s /usr/lib/go-1.8/bin/go /usr/bin/go \  
&& git clone -b "v$VERSION" \--single-branch
https://github.com/grafana/grafana.git . \  
&& if [ -n "$CC" ]; then \  
export CC=$CC && \  
export CGO_ENABLED=1 && \  
export GOOS=linux && \  
export GOARCH=$CC_GOARCH ; \  
fi \  
&& echo 'Building grafana-server ...' \  
&& go build -o dist/grafana-server ./pkg/cmd/grafana-server \  
&& echo 'Building the frontend ...' \  
&& wget -O /tmp/node.tar.xz
https://nodejs.org/dist/v6.11.2/node-v6.11.2-linux-x64.tar.xz \  
&& cd /usr/local \  
&& tar --strip-components=1 -xf /tmp/node.tar.xz \  
&& rm /tmp/node.tar.xz \  
&& cd /go/src/github.com/grafana/grafana \  
&& npm install -g yarn \  
&& yarn install --pure-lockfile \  
&& npm install -g grunt-cli \  
&& grunt  
  
FROM debian:stable-slim  
  
LABEL maintainer "Viktor Adam <rycus86@gmail.com>"  
  
COPY \--from=builder /go/src/github.com/grafana/grafana/dist/grafana-server
/usr/sbin/grafana-server  
COPY \--from=builder /go/src/github.com/grafana/grafana/conf/defaults.ini
/usr/share/grafana/conf/defaults.ini  
COPY \--from=builder /go/src/github.com/grafana/grafana/conf/sample.ini
/etc/grafana/grafana.ini  
COPY \--from=builder /go/src/github.com/grafana/grafana/public_gen
/usr/share/grafana/public  
COPY \--from=builder /go/src/github.com/grafana/grafana/scripts
/usr/share/grafana/scripts  
COPY \--from=builder /go/src/github.com/grafana/grafana/vendor
/usr/share/grafana/vendor  
  
EXPOSE 3000  
VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]  
ENTRYPOINT [ "/usr/sbin/grafana-server" ]  
CMD [ "--homepath=/usr/share/grafana", \  
"--config=/etc/grafana/grafana.ini", \  
"cfg:default.log.mode=console", \  
"cfg:default.paths.data=/var/lib/grafana", \  
"cfg:default.paths.logs=/var/log/grafana", \  
"cfg:default.paths.plugins=/var/lib/grafana/plugins" ]  

