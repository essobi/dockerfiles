FROM python:2-alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
FABRIC_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
build-base \  
curl \  
libffi-dev \  
openssl-dev \  
&& apk add --no-cache --no-progress \  
ca-certificates \  
libffi \  
\  
# Install fabric/fabric  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/fabric/fabric/${FABRIC_VERSION}" | xargs) \  
&& pip install \  
"fabric==${FABRIC_VERSION}" \  
\  
# Install sebastien/cuisine  
\  
&& pip install \  
cuisine \  
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
&& apk del \  
BUILD_DEPS \  
&& rm -f -r \  
/root/.cache \  
/tmp/*  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

