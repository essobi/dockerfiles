FROM debian:stable-slim  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_KEEP_ENV=1 \  
S6_READ_ONLY_ROOT=1 \  
VSFTPD_VERSION=latest  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& export BUILD_DEPS="build-essential curl gcc libpam0g-dev libssl-dev
libwrap0-dev" \  
&& apt-get install --no-install-recommends --yes \  
${BUILD_DEPS} \  
apache2-utils \  
ca-certificates \  
libpam-pwdfile \  
libssl-dev \  
libwrap0 \  
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
# Install vsftpd  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/_/vsftpd/latest" | xargs) \  
&& curl --location
"https://security.appspot.com/downloads/vsftpd-${VSFTPD_VERSION}.tar.gz" | tar
--directory /tmp --extract --gzip \  
&& make --directory "/tmp/vsftpd-${VSFTPD_VERSION}" \  
&& cp "/tmp/vsftpd-${VSFTPD_VERSION}/vsftpd" /usr/sbin/vsftpd \  
&& mkdir /usr/share/vsftpd \  
\  
# Configure user nobody  
\  
&& usermod --home /srv/ftp nobody \  
\  
# Clean  
\  
&& apt-get remove --purge --yes \  
${BUILD_DEPS} \  
&& apt-get autoremove --purge --yes \  
&& rm --force --recursive \  
/tmp/*  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "/init" ]  

