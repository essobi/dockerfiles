FROM alpine:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
REST_SERVER_VERSION=latest \  
RESTIC_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
bzip2 \  
curl \  
&& apk add --no-cache --no-progress \  
apache2-utils \  
ca-certificates \  
\  
# Install restic/rest-server  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/restic/rest-server/${REST_SERVER_VERSION}" | xargs) \  
&& curl --location --output /tmp/rest-server.gz
"https://github.com/restic/rest-
server/releases/download/v${REST_SERVER_VERSION}/rest-
server-${REST_SERVER_VERSION}-linux-amd64.gz" \  
&& gunzip /tmp/rest-server.gz \  
&& mv /tmp/rest-server /usr/bin/rest-server \  
&& chmod +x /usr/bin/rest-server \  
\  
# Install restic/restic  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/restic/restic/${RESTIC_VERSION}" | xargs) \  
&& curl \--location --output /tmp/restic.bz2
"https://github.com/restic/restic/releases/download/v${RESTIC_VERSION}/restic_${RESTIC_VERSION}_linux_amd64.bz2"
\  
&& bunzip2 /tmp/restic.bz2 \  
&& mv /tmp/restic /usr/bin/restic \  
&& chmod +x /usr/bin/restic \  
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

