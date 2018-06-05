  
FROM alpine:3.5  
  
ENV \  
ALPINE_MIRROR="dl-cdn.alpinelinux.org" \  
ALPINE_VERSION="v3.5" \  
TERM=xterm \  
BUILD_DATE="2017-04-21" \  
GOLANG_VERSION="1.8.1" \  
GOPATH=/opt/go \  
GOROOT=/usr/lib/go \  
APK_ADD="ca-certificates bash curl gcc musl-dev openssl go"  
  
LABEL org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Go Docker Image" \  
org.label-schema.description="Inofficial golang Docker Image" \  
org.label-schema.url="https://golang.org/" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-golang" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${GOLANG_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="GNU General Public License v3.0"  
  
#
---------------------------------------------------------------------------------------  
  
# https://golang.org/issue/14851  
COPY no-pic.patch /  
  
RUN \  
echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main" >
/etc/apk/repositories && \  
echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >>
/etc/apk/repositories && \  
apk --quiet --no-cache update && \  
apk --quiet --no-cache upgrade && \  
for apk in ${APK_ADD} ; \  
do \  
apk --quiet --no-cache add --virtual build-deps ${apk} ; \  
done && \  
export GOROOT_BOOTSTRAP="$(go env GOROOT)" && \  
curl \  
\--silent \  
\--location \  
\--retry 3 \  
"https://golang.org/dl/go${GOLANG_VERSION}.src.tar.gz" \  
| gunzip \  
| tar x -C /usr/local && \  
cd /usr/local/go/src && \  
patch -p2 -i /no-pic.patch && \  
./make.bash && \  
rm -rf /*.patch && \  
apk --purge del \  
build-deps && \  
mkdir /usr/lib/go && \  
mv /usr/local/go/bin /usr/lib/go/ && \  
mv /usr/local/go/lib /usr/lib/go/ && \  
mv /usr/local/go/pkg /usr/lib/go/ && \  
mv /usr/local/go/src /usr/lib/go/ && \  
ln -s /usr/lib/go/bin/go /usr/bin/go && \  
ln -s /usr/lib/go/bin/gofmt /usr/bin/gofmt && \  
rm -rf /usr/local/go && \  
unset GOROOT_BOOTSTRAP=  

