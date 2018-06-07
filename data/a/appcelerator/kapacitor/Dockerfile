FROM appcelerator/alpine:3.5.2  
ENV KAPACITOR_VERSION 1.2.0  
ENV GOLANG_VERSION 1.8  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
406865f587b44be7092f206d73fc1de252600b79b3cacc587b74b5ef5c623596  
  
RUN apk update && apk upgrade && \  
apk -v --virtual build-deps add --update go openssl python git gcc musl-dev &&
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
go get -v github.com/influxdata/kapacitor && \  
cd $GOPATH/src/github.com/influxdata/kapacitor && \  
git checkout -q --detach "v${KAPACITOR_VERSION}" && \  
python ./build.py && \  
mv ./build/kapacitor* /bin/ && \  
mkdir -p /var/lib/kapacitor && \  
apk del build-deps && cd / && rm -rf /var/cache/apk/* $GOPATH /usr/local/go  
  
EXPOSE 9092  
ENV INFLUXDB_URL http://localhost:8086  
ENV INFLUXDB_DB telegraf  
ENV INFLUXDB_RP default  
  
ADD run.sh /run.sh  
ADD kapacitor.conf /etc/kapacitor/kapacitor.conf.tpl  
ADD e494ce6c-d063-46f8-9d71-9030a29eef4b.srpl
/var/lib/kapacitor/replay/e494ce6c-d063-46f8-9d71-9030a29eef4b.srpl  
  
VOLUME /var/lib/kapacitor  
  
ENTRYPOINT ["/bin/sh", "-c"]  
CMD ["/run.sh"]  
  
HEALTHCHECK \--interval=10s --retries=3 --timeout=5s CMD curl -I
127.0.0.1:9092/kapacitor/v1/ping | grep -q "HTTP/1.1 204 No Content"  
  
LABEL axway_image=kapacitor  
# will be updated whenever there's a new commit  
LABEL commit=${GIT_COMMIT}  
LABEL branch=${GIT_BRANCH}  

