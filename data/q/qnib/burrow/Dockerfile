FROM qnib/alpn-consul  
  
ENV BURROW_ZK_HOST=zookeeper \  
BURROW_LOGFILE=/var/log/burrow/burrow.log  
VOLUME ["/var/log/burrow"]  
  
ENV GOLANG_VERSION 1.7.3  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
79430a0027a09b0b3ad57e214c4c1acfdd7af290961dd08d322818895af1ef44  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go \  
\  
&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
\  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/go/src \  
&& ./make.bash \  
\  
&& rm -rf /*.patch \  
&& apk del .build-deps  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
RUN apk add --no-cache curl bash git ca-certificates wget go \  
&& update-ca-certificates \  
&& curl -sSO https://raw.githubusercontent.com/pote/gpm/v1.4.0/bin/gpm \  
&& chmod +x gpm \  
&& mv gpm /usr/local/bin  
  
RUN mkdir -p $GOPATH/src/github.com/linkedin/Burrow \  
&& cd $GOPATH/src/github.com/linkedin/Burrow \  
&& wget -qO - https://github.com/linkedin/Burrow/archive/v0.1.1.tar.gz |tar
xfz - --strip-components=1 \  
&& gpm install \  
&& go install \  
&& mv $GOPATH/bin/Burrow $GOPATH/bin/burrow \  
&& apk del git wget go  
  
ADD etc/consul-templates/burrow/burrow.cfg.ctmpl \  
etc/consul-templates/burrow/logging.cfg.ctmpl \  
etc/consul-templates/burrow/  
ADD opt/qnib/burrow/bin/start.sh \  
/opt/qnib/burrow/bin/  
ADD etc/supervisord.d/burrow.ini /etc/supervisord.d/  
ADD etc/consul.d/burrow.json /etc/consul.d/  
  

