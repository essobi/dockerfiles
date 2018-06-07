FROM debian:stable-slim  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
BOOTSTRAP_VERSION=latest \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_KEEP_ENV=1 \  
S6_OVERLAY_VERSION=latest \  
S6_READ_ONLY_ROOT=1  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& export BUILD_DEPS="ca-certificates curl unzip" \  
&& apt-get install --no-install-recommends --yes \  
${BUILD_DEPS} \  
nginx-full \  
openssh-server \  
\  
# Install bootstrap  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/twbs/bootstrap/${BOOTSTRAP_VERSION}" | xargs) \  
&& curl --location --output /tmp/bootstrap.zip
"https://github.com/twbs/bootstrap/releases/download/v${BOOTSTRAP_VERSION}/bootstrap-${BOOTSTRAP_VERSION}-dist.zip"
\  
&& unzip /tmp/bootstrap.zip -d /tmp \  
&& mkdir --parents /var/www/css \  
&& mv "/tmp/bootstrap-${BOOTSTRAP_VERSION}-dist/css/bootstrap.min.css"
/var/www/css/bootstrap.min.css \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/s6-overlay/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/syslog-stdout/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
\  
# Configure user "www-data"  
\  
&& usermod --append --groups shadow www-data \  
\  
# Create missing folders  
\  
&& mkdir --parents \  
/etc/seedbox \  
/run/sshd \  
/var/lib/seedbox \  
/var/log/nginx \  
\  
# Clean  
\  
&& apt-get remove --purge --yes \  
${BUILD_DEPS} \  
&& apt-get autoremove --purge --yes \  
&& rm --force --recursive \  
/etc/ssh/ssh_host_* \  
/tmp/* \  
/var/lib/apt/lists/*  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "/init" ]  

