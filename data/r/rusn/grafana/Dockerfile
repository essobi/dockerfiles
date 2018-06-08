FROM alpine:3.3  
MAINTAINER Nikita Rusin <rusinnick@gmail.com>  
  
ENV GOPATH=/go \  
REPO_PATH=github.com/grafana/grafana \  
REPO_TAG=v2.6.0  
RUN apk add --update --virtual build-deps \  
go nodejs build-base git mercurial \  
&& git clone https://$REPO_PATH.git -b $REPO_TAG \--depth 1 \  
/go/src/$REPO_PATH \  
&& cd /go/src/$REPO_PATH \  
&& go run build.go setup \  
&& /go/bin/godep restore \  
&& go run build.go build \  
&& npm install --unsafe-perm \  
&& npm install -g grunt-cli \  
&& grunt \  
&& mkdir -p /grafana /grafana/conf \  
&& cp ./bin/grafana-server /grafana/grafana-server \  
&& cp -r ./public_gen /grafana/public \  
&& cp conf/*.ini /grafana/conf \  
&& rm -rf /go \  
&& apk del --purge build-deps \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* \  
&& rm -rf /root/.n*  
  
WORKDIR /grafana  
  
ADD config.ini /grafana/conf/config.ini  
  
EXPOSE 3000  
VOLUME ["/data"]  
  
ENTRYPOINT ["./grafana-server"]  
CMD ["-config=conf/config.ini"]

