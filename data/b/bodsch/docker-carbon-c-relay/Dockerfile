  
FROM alpine:3.6  
  
MAINTAINER Bodo Schulz <bodo@boone-schulz.de>  
  
ENV \  
ALPINE_MIRROR="mirror1.hs-esslingen.de/pub/Mirrors" \  
ALPINE_VERSION="v3.6" \  
TERM=xterm \  
BUILD_DATE="2017-08-29" \  
VERSION="3.1" \  
GOPATH=/opt/go \  
APK_ADD="curl g++ git make musl-dev"  
  
EXPOSE 2003  
  
LABEL \  
version="1708-35" \  
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
  
RUN \  
echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main" >
/etc/apk/repositories && \  
echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >>
/etc/apk/repositories && \  
apk --no-cache update && \  
apk --no-cache upgrade && \  
apk --no-cache add ${APK_ADD} && \  
mkdir /opt && \  
  
echo "https://github.com/grobian/carbon-c-relay/archive/v${VERSION}.tar.gz" &&
\  
curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/ca-certificates.crt \  
https://github.com/grobian/carbon-c-relay/archive/v${VERSION}.tar.gz \  
| gunzip \  
| tar x -C /opt/ && \  
cd /opt/carbon-c-relay-${VERSION} && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
apk --purge del ${APK_ADD} && \  
rm -rf \  
/opt/* \  
/tmp/* \  
/var/cache/apk/*  
  
COPY rootfs/ /  
  
CMD [ "/init/run.sh" ]  
  
#
---------------------------------------------------------------------------------------  

