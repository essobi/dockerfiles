  
FROM alpine:3.7  
  
ENV \  
TERM=xterm \  
BUILD_DATE="2018-05-04" \  
BUILD_TYPE="stable" \  
BUILD_VERSION="2.2.8" \  
QUASSEL_HOST=localhost \  
QUASSEL_PORT=4242 \  
FORCE_DEFAULT=true \  
WEBSERVER_MODE=http \  
WEBSERVER_PORT=64080  
  
EXPOSE 64080  
  
LABEL \  
version="1802" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Quassel Webserver Docker Image" \  
org.label-schema.description="Inofficial Quassel Webserver Docker Image" \  
org.label-schema.url="https://github.com/magne4000/quassel-webserver" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-quassel-web" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${ICINGA_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU General Public License v3.0"  
#
---------------------------------------------------------------------------------------  
  
RUN \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --quiet --no-cache --virtual .build-deps \  
build-base curl git python && \  
apk add --quiet --no-cache \  
nodejs \  
nodejs-npm \  
openssl && \  
mkdir /data && \  
cd /data && \  
git clone https://github.com/magne4000/quassel-webserver.git && \  
cd quassel-webserver && \  
if [ "${BUILD_TYPE}" == "stable" ] ; then \  
echo "switch to stable Tag v${BUILD_VERSION}" && \  
git checkout tags/${BUILD_VERSION} 2> /dev/null ; \  
fi && \  
npm i -g npm && \  
npm install acorn && \  
npm install --production && \  
npm ls -gp --depth=0 | awk -F/node_modules/ '{print $2}' | grep -vE '^(npm|)$'
| xargs -r npm -g rm && \  
apk del --quiet .build-deps && \  
rm -rf \  
/tmp/* \  
/root/.n* \  
/data/quassel-webserver/.git* \  
/var/cache/apk/*  
  
ADD rootfs/ /  
  
WORKDIR /data/quassel-webserver  
  
CMD ["/init/run.sh"]  

