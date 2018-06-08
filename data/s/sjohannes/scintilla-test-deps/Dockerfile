# Copying and distribution of this file, with or without modification,  
# are permitted in any medium without royalty.  
# This file is offered as-is, without any warranty.  
  
FROM debian:unstable-slim  
  
RUN set -x \  
&& sed -i 's/deb\\.debian\\.org/httpredir.debian.org/' /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends eatmydata \  
&& eatmydata apt-get install -y --no-install-recommends \  
g++ \  
g++-mingw-w64-x86-64 \  
libgtk2.0-dev \  
libgtk-3-dev \  
libpyside-dev \  
libqt4-dev \  
libshiboken-dev \  
make \  
pkg-config \  
python-pyside.qtgui \  
shiboken \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  

