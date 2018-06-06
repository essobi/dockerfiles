FROM ruby:2.3-alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
MAILCATCHER_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
build-base \  
ca-certificates \  
curl \  
sqlite-dev \  
&& apk add --no-cache --no-progress \  
libstdc++ \  
sqlite-libs \  
\  
# Install sj26/mailcatcher  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/sj26/mailcatcher/${MAILCATCHER_VERSION}" | xargs) \  
&& gem install --no-rdoc --no-ri --no-verbose \  
"mailcatcher:${MAILCATCHER_VERSION}" \  
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
BUILD_DEPS  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

