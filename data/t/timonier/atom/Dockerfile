FROM ubuntu:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
ATOM_VERSION=latest \  
NO_AT_BRIDGE=1  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& apt-get install --no-install-recommends --yes \  
ca-certificates \  
curl \  
gconf2 \  
gconf-service \  
git \  
gtk2-engines-murrine \  
gvfs-bin \  
libasound2 \  
libatk-adaptor \  
libcanberra-gtk-module \  
libgail-common \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libx11-xcb1 \  
libxkbfile1 \  
libxss1 \  
libxtst6 \  
locales \  
overlay-scrollbar-gtk2 \  
python \  
unity-gtk2-module \  
wget \  
xdg-utils \  
\  
# Install atom/atom  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/atom/atom/${ATOM_VERSION}" | xargs) \  
&& curl --location --output /tmp/atom.deb
"https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-
amd64.deb" \  
&& dpkg --install /tmp/atom.deb \  
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
&& rm --force --recursive \  
/tmp/* \  
/var/lib/apt/lists/*  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

