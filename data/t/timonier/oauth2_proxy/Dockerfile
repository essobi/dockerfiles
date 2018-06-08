FROM alpine:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
OAUTH2_PROXY_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
curl \  
&& apk add --no-cache --no-progress \  
ca-certificates \  
\  
# Install bitly/oauth2_proxy  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/bitly/oauth2_proxy/${OAUTH2_PROXY_VERSION}" | xargs) \  
&& curl --location
"https://github.com/bitly/oauth2_proxy/releases/download/${OAUTH2_PROXY_TAG}/oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-
amd64.go${OAUTH2_PROXY_GO_VERSION}.tar.gz" | tar --directory /tmp --extract
--gzip \  
&& mv "/tmp/oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-
amd64.go${OAUTH2_PROXY_GO_VERSION}/oauth2_proxy" /usr/bin/oauth2_proxy \  
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
  
ENTRYPOINT [ "dumb-entrypoint" ]  

