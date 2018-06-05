FROM python:alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
STORM_VERSION=latest  
  
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
# Install emre/storm  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/emre/storm/${STORM_VERSION}" | xargs) \  
&& pip install \  
"stormssh==${STORM_VERSION}" \  
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
/root/.cache \  
/tmp/*  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

