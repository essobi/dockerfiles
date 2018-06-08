FROM ubuntu:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
NO_AT_BRIDGE=1 \  
OPENOFFICE_LANG=en-US \  
OPENOFFICE_VERSION=latest  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& export BUILD_DEPS="curl" \  
&& apt-get install --no-install-recommends --yes \  
${BUILD_DEPS} \  
ca-certificates \  
default-jre \  
libxt6 \  
locales \  
\  
# Install dagwieers/unoconv  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/dagwieers/unoconv/latest" | xargs) \  
&& curl --location
"https://github.com/dagwieers/unoconv/archive/${UNOCONV_VERSION}.tar.gz" | tar
--directory /tmp --extract --gzip \  
&& mv "/tmp/unoconv-${UNOCONV_VERSION}" /opt/unoconv \  
\  
# Install openoffice  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/_/openoffice/${OPENOFFICE_VERSION}" | xargs) \  
&& curl --location
"https://sourceforge.net/projects/openofficeorg.mirror/files/${OPENOFFICE_VERSION}/binaries/${OPENOFFICE_LANG}/Apache_OpenOffice_${OPENOFFICE_VERSION}_Linux_x86-64_install-
deb_${OPENOFFICE_LANG}.tar.gz/download" | tar --directory /tmp --extract
--gzip \  
&& dpkg --install /tmp/${OPENOFFICE_LANG}/DEBS/*.deb \  
&& dpkg --install /tmp/${OPENOFFICE_LANG}/DEBS/desktop-integration/*.deb \  
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
  
COPY ./rootfs /  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

