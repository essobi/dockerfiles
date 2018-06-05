FROM debian:jessie  
MAINTAINER iaroki  
RUN apt-get update && apt-get install -y \  
git \  
gconf2 \  
gconf-service \  
gvfs-bin \  
libasound2 \  
libcap2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libxkbfile1 \  
libxss1 \  
libxtst6 \  
xdg-utils \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
ENV ATOM_VERSION=1.15.0  
RUN buildDeps=' \  
ca-certificates \  
curl \  
' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sSL
https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-amd64.deb
-o /tmp/atom-amd64.deb \  
&& dpkg -i /tmp/atom-amd64.deb \  
&& rm -rf /tmp/*.deb \  
&& apt-get purge -y --auto-remove $buildDeps  
RUN useradd -m -u 1000 -G video iaroki  
USER iaroki  
WORKDIR /home/iaroki  
ENTRYPOINT ["atom", "--foreground"]  

