FROM debian:stretch-slim  
LABEL github "https://github.com/mrorgues"  
#============================#  
# Information & Requirements #  
#============================#  
# *** Run haroopad desktop app in a container ***  
#  
# docker run --rm -it \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# --device /dev/dri \  
# -v "${HOME}/.config/Haroopad:/root/.config/Haroopad" \  
# --name haroopad \  
# mrorgues/haroopad  
#========#  
# Basics #  
#========#  
RUN apt-get update && apt-get install -y \  
libasound2 \  
desktop-file-utils \  
gconf2 \  
libcanberra-gtk-module \  
libgtk2.0-0 \  
libnotify-bin \  
libnss3 \  
libxtst6 \  
python \  
xdg-utils \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
  
#==========#  
# Haroopad #  
#==========#  
ENV VERSION 0.13.1  
ENV DOWNLOAD_URL https://bitbucket.org/rhiokim/haroopad-
download/downloads/haroopad-v${VERSION}-x64.deb  
RUN buildDeps='\  
curl \  
ca-certificates \  
' && \  
set -x && \  
apt-get update && apt-get install -y $buildDeps --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sSL "${DOWNLOAD_URL}" > /tmp/haroopad.deb && \  
dpkg -i /tmp/haroopad.deb && \  
rm -rf /tmp/haroopad.deb && \  
apt-get purge -y --auto-remove $buildDeps  
  
  
#=============#  
# Here we go! #  
#=============#  
ENTRYPOINT ["/usr/bin/haroopad"]  

