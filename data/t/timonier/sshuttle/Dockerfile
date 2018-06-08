FROM python:slim  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
SSHUTTLE_VERSION=latest  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& export BUILD_DEPS="curl git" \  
&& apt-get install --no-install-recommends --yes \  
${BUILD_DEPS} \  
ca-certificates \  
iptables \  
ssh-client \  
\  
# Install sshuttle/sshuttle  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/sshuttle/sshuttle/${SSHUTTLE_VERSION}" | xargs) \  
&& git clone --branch "v${SSHUTTLE_VERSION}"
"https://github.com/sshuttle/sshuttle.git" /tmp/sshuttle \  
&& sh -c "cd /tmp/sshuttle && ./setup.py install" \  
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
&& apt-get remove --purge --yes \  
${BUILD_DEPS} \  
&& apt-get autoremove --purge --yes \  
&& rm --force --recursive \  
/tmp/* \  
/var/lib/apt/lists/*  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

