FROM golang:alpine as drive  
  
ENV \  
DRIVE_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress \  
build-base \  
curl \  
git \  
\  
# Install odeke-em/drive  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/odeke-em/drive/${DRIVE_VERSION}" | xargs) \  
&& mkdir -p "${GOPATH}/src/github.com/odeke-em/drive" \  
&& git clone "https://github.com/odeke-em/drive.git"
"${GOPATH}/src/github.com/odeke-em/drive" \  
&& git -C "${GOPATH}/src/github.com/odeke-em/drive" checkout
"v${DRIVE_VERSION}" \  
&& go get github.com/odeke-em/drive/cmd/drive  
  
# ---  
  
FROM alpine:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
DRIVE_VERSION=latest  
  
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
/tmp/*  
  
COPY --from=drive /go/bin/drive /usr/bin/drive  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

