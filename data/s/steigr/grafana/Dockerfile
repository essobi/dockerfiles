FROM alpine:3.5  
MAINTAINER \  
[Nicolas Degory <ndegory@axway.com>]\  
[Mathias Kaufmann <me@stei.gr>]  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "@community http://nl.alpinelinux.org/alpine/v3.5/community" >>
/etc/apk/repositories  
  
RUN apk upgrade --no-cache \  
&& apk --no-cache add --virtual .runtime-dep curl su-exec@testing bash \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -Lo /tmp/tini.apk
http://nl.alpinelinux.org/alpine/edge/community/x86_64/tini-0.14.0-r0.apk \  
&& apk add --virtual .runtime-dep /tmp/tini.apk \  
&& rm -rf /tmp/tini.apk  
  
RUN curl -L https://github.com/subfuzion/envtpl/blob/master/envtpl?raw=true \  
| install -m 0755 -o root -g root /dev/stdin /usr/bin/envtpl  
  
RUN apk --no-cache add --virtual .runtime-dep nodejs  
  
ARG GRAFANA_VERSION=${GRAFANA_VERSION:-v4.1.2}  
  
RUN apk upgrade --no-cache \  
&& apk --no-cache add --virtual .runtime-dep fontconfig \  
&& rm -rf /var/cache/apk/*  
  
RUN export GOPATH=/go \  
&& apk upgrade --no-cache \  
&& apk --no-cache add --virtual .build-dep build-base go git gcc python musl-
dev make nodejs-dev fontconfig-dev \  
&& mkdir -p $GOPATH/src/github.com/grafana \  
&& sh -xc "[[ '${GRAFANA_VERSION:0:1}' = 'v' ]] || GRAFANA_VERSION=master; git
clone https://github.com/grafana/grafana.git -b ${GRAFANA_VERSION}
$GOPATH/src/github.com/grafana/grafana" \  
&& cd $GOPATH/src/github.com/grafana/grafana \  
&& npm install -g yarn@0.19.0 \  
&& npm install -g grunt-cli@1.2.0 \  
&& go run build.go setup \  
&& go run build.go build \  
&& yarn install \  
&& npm run build \  
&& npm uninstall -g yarn \  
&& npm uninstall -g grunt-cli \  
&& npm cache clear \  
&& mv ./bin/grafana-server ./bin/grafana-cli /bin/ \  
&& mkdir -p /etc/grafana/json \  
/var/lib/grafana/plugins \  
/var/log/grafana \  
/usr/share/grafana \  
&& mv ./public_gen /usr/share/grafana/public \  
&& mv ./conf /usr/share/grafana/conf \  
&& apk del .build-dep \  
&& cd / \  
&& rm -rf /var/cache/apk/* \  
/usr/local/share/.cache \  
$GOPATH  
  
VOLUME ["/var/lib/grafana", "/var/lib/grafana/plugins", "/var/log/grafana"]  
  
EXPOSE 3000  
ENV TINI_SUBREAPER= \  
INFLUXDB_HOST=localhost \  
INFLUXDB_PORT=8086 \  
INFLUXDB_PROTO=http \  
INFLUXDB_USER=grafana \  
INFLUXDB_PASS=changeme \  
GRAFANA_USER=admin \  
GRAFANA_PASS=changeme  
  
#ENV GRAFANA_BASE_URL  
#ENV FORCE_HOSTNAME  
HEALTHCHECK \--interval=5s --retries=5 --timeout=2s CMD curl -u
$GRAFANA_USER:$GRAFANA_PASS 127.0.0.1:3000/api/org 2>/dev/null | grep -q
'"id":'  
  
RUN addgroup -S grafana \  
&& adduser -S -g grafana grafana  
  
ENTRYPOINT ["tini"]  
CMD ["/run.sh"]  
COPY ./run.sh /run.sh  
  
COPY ./grafana.ini /usr/share/grafana/conf/defaults.ini.tpl  
  
# label-schema.org  
ARG LABEL_NAME="${LABEL_NAME:-grafana}"  
ARG LABEL_DESCRIPTION="${LABEL_DESCRIPTION:-Beautiful metric & analytic
dashboards}"  
ARG LABEL_BUILD_DATE="${LABEL_BUILD_DATE:-2017/3/1}"  
ARG LABEL_VCS_REF="${LABEL_VCS_REF:-unknown}"  
ARG LABEL_VCS_URL="${LABEL_VCS_URL:-https://github.com/steigr/docker-grafana}"  
ARG LABEL_URL="${LABEL_URL:-https://grafana.org}"  
LABEL org.label-schema.build-date="${LABEL_BUILD_DATE}" \  
org.label-schema.name="${LABEL_NAME}" \  
org.label-schema.description="${LABEL_DESCRIPTION}" \  
org.label-schema.usage="${LABEL_VCS_URL}/blob/${GRAFANA_VERSION}/README.md" \  
org.label-schema.url="${LABEL_URL}" \  
org.label-schema.vcs-ref="${LABEL_VCS_REF}" \  
org.label-schema.vcs-url="${LABEL_VCS_URL}" \  
org.label-schema.version="${GRAFANA_VERSION}" \  
org.label-schema.docker.cmd="docker run --detach --name=${LABEL_NAME}
\--publish=3000:3000 --volume=${LABEL_NAME}:/var/lib/grafana
--volume=${LABEL_NAME}-plugins:/var/lib/grafana/plugins
steigr/${LABEL_NAME}:${GRAFANA_VERSION}" \  
org.label-schema.docker.params="INFLUXDB_HOST=hostname or address of influxdb
server,\  
INFLUXDB_PORT=portnumber where influxdb is listening,\  
INFLUXDB_PROTO=protocol used for influxdb connection,\  
INFLUXDB_USER=influxdb username,\  
INFLUXDB_PASS=influxdb password,\  
GRAFANA_USER=administration username,\  
GRAFANA_PASS=grafana administrator password,\  
GRAFANA_BASE_URL=url of this grafana instance,\  
FORCE_HOSTNAME=force this hostname"  

