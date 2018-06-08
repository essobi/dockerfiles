FROM alpine  
  
EXPOSE 3000  
  
ENV GOPATH=/tmp/go  
ENV ORCHESTRATOR_REPO=https://github.com/github/orchestrator.git  
ENV ORCHESTRATOR_VERSION=tags/v2.1.5  
ENV DOCKERIZE_VERSION v0.5.0  
  
RUN set -ex \  
&& apk add --update --no-cache \  
bash \  
mysql-client \  
curl \  
rsync \  
redis \  
jq \  
&& cd /tmp \  
&& curl -sLO
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& apk add --update --no-cache --virtual .build-deps \  
git \  
go \  
build-base \  
&& mkdir -p "$GOPATH/src/github.com/github/orchestrator" \  
&& git clone "$ORCHESTRATOR_REPO" "$GOPATH/src/github.com/github/orchestrator"
\  
&& cd $GOPATH/src/github.com/github/orchestrator \  
&& git checkout "$ORCHESTRATOR_VERSION" \  
&& bash build.sh -b \  
&& rsync -av $(find /tmp/orchestrator-release -type d -name orchestrator
-maxdepth 2)/ / \  
&& ln -sf /usr/local/orchestrator/orchestrator /usr/bin/orchestrator \  
&& cp "$GOPATH/src/github.com/github/orchestrator/docker/entrypoint.sh"
/entrypoint.sh \  
&& cd / \  
&& apk del .build-deps \  
&& rm -rf /tmp/*  
  
WORKDIR /usr/local/orchestrator  
CMD /entrypoint.sh  

