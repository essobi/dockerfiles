  
FROM golang:1.10-alpine as builder  
  
ENV \  
TERM=xterm \  
BUILD_DATE="2018-05-04" \  
BUILD_TYPE="stable" \  
VERSION="0.10.1"  
#
---------------------------------------------------------------------------------------  
  
RUN \  
apk update --no-cache && \  
apk upgrade --no-cache && \  
apk add \  
g++ git make musl-dev && \  
echo "export BUILD_DATE=${BUILD_DATE}" >> /etc/enviroment && \  
echo "export BUILD_TYPE=${BUILD_TYPE}" >> /etc/enviroment && \  
echo "export VERSION=${VERSION}" >> /etc/enviroment  
  
RUN \  
export GOPATH=/opt/go && \  
mkdir -p ${GOPATH} && \  
export PATH="${PATH}:${GOPATH}/bin" && \  
go get -d github.com/graphite-ng/carbon-relay-ng || true && \  
go get github.com/jteeuwen/go-bindata/... && \  
cd ${GOPATH}/src/github.com/graphite-ng/carbon-relay-ng && \  
if [ "${BUILD_TYPE}" == "stable" ] ; then \  
echo "switch to stable Tag v${VERSION}" && \  
git checkout tags/${VERSION} 2> /dev/null ; \  
fi  
  
RUN \  
echo "build" && \  
export GOPATH=/opt/go && \  
cd ${GOPATH}/src/github.com/graphite-ng/carbon-relay-ng && \  
export PATH="${PATH}:${GOPATH}/bin" && \  
version=$(git describe --tags --always | sed 's/^v//') && \  
echo "build version: ${version}" && \  
make && \  
mv carbon-relay-ng /tmp/carbon-relay-ng && \  
cp -rv examples /tmp/  
#
---------------------------------------------------------------------------------------  
  
  
FROM alpine:3.7  
  
ENV \  
TERM=xterm \  
TZ='Europe/Berlin' \  
BUILD_DATE="2018-05-04"  
  
EXPOSE 2003 2004 8081  
  
LABEL \  
version="1805" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="carbon-relay-ng Docker Image" \  
org.label-schema.description="Inofficial carbon-relay-ng Docker Image" \  
org.label-schema.url="https://github.com/graphite-ng/carbon-relay-ng" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-docker-carbon-
relay-ng" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="The Unlicense"  
#
---------------------------------------------------------------------------------------  
  
WORKDIR /  
  
COPY --from=builder /tmp/carbon-relay-ng /usr/bin/carbon-relay-ng  
COPY --from=builder /tmp/examples/storage-schemas.conf /etc/carbon-relay-
ng/storage-schemas.conf  
COPY --from=builder /tmp/examples/carbon-relay-ng.ini /etc/carbon-relay-
ng/carbon-relay-ng.ini  
  
RUN \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --no-cache --quiet --virtual .build-deps \  
tzdata && \  
cp /usr/share/zoneinfo/${TZ} /etc/localtime && \  
echo ${TZ} > /etc/timezone && \  
apk --quiet --purge del .build-deps && \  
mkdir -p /var/spool/carbon-relay-ng && \  
chown nobody: /var/spool/carbon-relay-ng && \  
rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
COPY rootfs/ /  
  
HEALTHCHECK \  
\--interval=5s \  
\--timeout=2s \  
\--retries=12 \  
\--start-period=10s \  
CMD ps ax | grep -v grep | grep -c "/usr/bin/carbon-relay-ng" || exit 1  
  
CMD [ "/init/run.sh" ]  
  
# EOF  

