FROM appcelerator/alpine:3.5.2  
ENV INFLUXDB_VERSION 1.2.2  
ENV GOLANG_VERSION 1.8  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
406865f587b44be7092f206d73fc1de252600b79b3cacc587b74b5ef5c623596  
  
RUN apk update && apk upgrade && \  
apk --virtual build-deps add go python openssl git gcc musl-dev make patch &&
\  
export GOROOT_BOOTSTRAP="$(go env GOROOT)" && \  
wget -q "$GOLANG_SRC_URL" -O golang.tar.gz && \  
echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - && \  
tar -C /usr/local -xzf golang.tar.gz && \  
rm golang.tar.gz && \  
cd /usr/local/go/src && \  
./make.bash && \  
export GOPATH=/go && \  
export PATH=/usr/local/go/bin:$PATH && \  
go version && \  
go get -v github.com/influxdata/influxdb && \  
cd $GOPATH/src/github.com/influxdata/influxdb && \  
git checkout -q --detach "v${INFLUXDB_VERSION}" && \  
python ./build.py && \  
chmod +x ./build/influx* && \  
mv ./build/influx* /bin/ && \  
mkdir -p /etc/influxdb /data/influxdb /data/influxdb/meta /data/influxdb/data
/var/tmp/influxdb/wal /var/log/influxdb && \  
apk del build-deps && cd / && rm -rf $GOPATH/ /var/cache/apk/* /usr/local/go  
  
RUN apk update && apk add util-linux && rm -rf /var/cache/apk/*  
  
ENV ADMIN_USER root  
ENV INFLUXDB_INIT_PWD root  
  
ADD types.db /usr/share/collectd/types.db  
ADD config.toml /etc/influxdb/config.toml.tpl  
ADD run.sh /run.sh  
  
ENV PRE_CREATE_DB **None**  
  
# Admin server WebUI  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
VOLUME ["/data"]  
  
ENTRYPOINT ["/bin/sh", "-c"]  
CMD ["/run.sh"]  
  
HEALTHCHECK \--interval=5s --retries=24 --timeout=1s CMD curl -sI
127.0.0.1:8086/ping | grep -q "204 No Content"  

