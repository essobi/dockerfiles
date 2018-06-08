FROM golang:alpine as license  
  
ENV \  
LICENSE_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress \  
build-base \  
curl \  
git \  
\  
# Install nishanths/license  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/nishanths/license/${LICENSE_VERSION}" | xargs) \  
&& mkdir -p "${GOPATH}/src/github.com/nishanths/license" \  
&& git clone "https://github.com/nishanths/license.git"
"${GOPATH}/src/github.com/nishanths/license" \  
&& git -C "${GOPATH}/src/github.com/nishanths/license" checkout
"v${LICENSE_VERSION}" \  
&& go get github.com/nishanths/license  
  
# ---  
  
FROM alpine:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
LICENSE_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
curl \  
&& apk add --no-cache --no-progress \  
ca-certificates \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-entrypoint/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/gosu/installer" | INSTALL_DIRECTORY="/usr/sbin" sh
-s -- install \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS \  
&& rm -f -r \  
/home \  
/tmp  
  
COPY --from=license /go/bin/license /usr/bin/license  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

